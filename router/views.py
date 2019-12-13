from django.shortcuts import render
import os
from django.http import JsonResponse
import pdb
import requests
import json
# Create your views here.

def index(request):
    mapBoxToken = os.environ['MAPBOXTOKEN']
    return render(request, 'router/map.html', {'token': mapBoxToken})

def route(request):
    origin = json.loads(request.POST['originCoor'])
    destination = json.loads(request.POST['destinationCoor'])
    modeTransport = request.POST['modeTransport']
    if (modeTransport == 'Walk'):
        modeTransport = 'foot'
    else:
        modeTransport = 'bike'
    api_key = os.environ['TOKEN']
    res = requests.get(f'https://graphhopper.com/api/1/route?point={origin[1]},{origin[0]}&point={destination[1]},{destination[0]}&vehicle={modeTransport}&key={api_key}&ch.disable=true&algorithm=alternative_route&alternative_route.max_paths=4&points_encoded=false')
    return JsonResponse(res.json())



