from django import forms

class MediaForm(forms.Form):
    city = forms.CharField(max_length=120, required=True)