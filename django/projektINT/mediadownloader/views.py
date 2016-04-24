from django.shortcuts import render
from .forms import MediaForm
from django.http import HttpResponse
# import zmq
import os
import binascii

# Create your views here.
def home(request):
    context = {}
    response = render(request, 'media.html', context)
    requestID = 0
    if 'id' not in request.COOKIES:
        requestID = binascii.hexlify(os.urandom(16))
    else:
        requestID = request.COOKIES['id']

    title = "What's up in ..."
    form = MediaForm(request.POST or None)
    confirm_message = None

    # if form.is_valid():
        # confirm_message = 'We are searching for new information'
        # contextZMQ = zmq.Context()
        # socket = contextZMQ.socket(zmq.REQ)
        # socket.connect ("tcp://localhost:5556")
        # socket.send_string("{{\"MediaApp\":{{\"requestID\": \"{reqID}\",\"application\": \"twitter\",\"request\": \"getTweetsByCord\",\"city\": \"{city}\"}}}}".format(city=form.cleaned_data['city'], reqID=requestID))
        # socket.recv()
        # socket.send_string("{{\"MediaApp\":{{\"requestID\": \"{reqID}\",\"application\": \"flickr\",\"request\": \"getPictureByCord\",\"city\": \"{city}\"}}}}".format(city=form.cleaned_data['city'], reqID=requestID))
        # form = None

    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message
    }
    
    response = render(request, 'media.html', context)
    if 'id' not in request.COOKIES:
    	response.set_cookie('id', requestID)
    return response