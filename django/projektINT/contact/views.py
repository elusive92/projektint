from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.
def home(request):
    title = "Contact us"
    form = ContactForm(request.POST or None)
    confirm_message = None
    
    if form.is_valid():
        name = "projektINT - " + form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        frm = form.cleaned_data['email']
        to_us = [settings.EMAIL_HOST_USER]
        send_mail(name, comment, frm, to_us, fail_silently=True)
        confirm_message = """
        Thank you for your message. We have received it and we are reviewing it.
        """
        form = None
    
    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
    }
    
    template  = 'contact.html'
    return render(request, template, context)