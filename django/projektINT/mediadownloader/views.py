from django.shortcuts import render
from .forms import MediaForm
import zmq

# Create your views here.
def home(request):
    title = "What's up in ..."
    form = MediaForm(request.POST or None)
    confirm_message = None
    
    if form.is_valid():
        confirm_message = 'We are searching for new information'
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://localhost:5556")
        socket.send_string("{{\"MediaApp\":{{\"requestID\": \"10\",\"application\": \"twitter\",\"request\": \"getTweetsByCord\",\"city\": \"{city}\"}}}}".format(city=form.cleaned_data['city']))
        socket.recv()
        socket.send_string("{{\"MediaApp\":{{\"requestID\": \"10\",\"application\": \"flickr\",\"request\": \"getPictureByCord\",\"city\": \"{city}\"}}}}".format(city=form.cleaned_data['city']))
        form = None
    
    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
    }
    
    template  = 'media.html'
    return render(request, template, context)