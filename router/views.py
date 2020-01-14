from django.shortcuts import render
import os
from django.http import JsonResponse
import pdb
import requests
import json
# Create your views here.

def index(request):
    mapBoxToken = os.environ['MAPBOXTOKEN']
    api_key = os.environ['TOKEN']
    return render(request, 'router/map.html', {'api_key': api_key, 'token': mapBoxToken})

def route(request):
    origin = json.loads(request.POST['originCoor'])
    destination = json.loads(request.POST['destinationCoor'])
    modeTransport = request.POST['modeTransport']
    if (modeTransport == 'Walk'):
        modeTransport = 'walking'
    else:
        modeTransport = 'bicycling'
    api_key = os.environ['TOKEN']
    res = requests.get(f'https://maps.googleapis.com/maps/api/directions/json?origin={origin[1]},{origin[0]}&destination={destination[1]},{destination[0]}&mode={modeTransport}&key={api_key}&alternatives=true')
    return JsonResponse(res.json())



