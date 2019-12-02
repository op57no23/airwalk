from django.shortcuts import render
import os
from django.http import JsonResponse
import pdb
import requests
import json
# Create your views here.

def index(request):
    token = os.environ['TOKEN']
    return render(request, 'router/map.html', {'token': token})

def route(request):
    origin = json.loads(request.POST['originCoor'])
    destination = json.loads(request.POST['destinationCoor'])
    token = os.environ['TOKEN']
    res = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/cycling/{origin[0]},{origin[1]};{destination[0]},{destination[1]}?access_token=pk.eyJ1IjoidXJiYW50aG9yZWF1IiwiYSI6ImNrM2MwbHozbzBlY3IzZW1hangwdDhqNWgifQ.YcoTSYtYcIcTYdBok-TZaQ&steps=true&alternatives=true&overview=full&geometries=geojson')
    return JsonResponse(json.dumps(res.json()['routes']), safe = False)

