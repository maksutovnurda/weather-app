from django.shortcuts import render
import uuid
import requests
from django.http import JsonResponse
from .models import Search
from datetime import datetime

# Create your views here.
def main(request):
    return render(request, 'main/index.html')


def get_weather(request):
    city = request.GET.get('city')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    visitor_id = request.COOKIES.get('visitor_id')
    if not visitor_id:
        visitor_id = str(uuid.uuid4())

    weather_response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
    data = weather_response.json()

    response = {
        'city': city,
        'latitude': latitude,
        'longitude': longitude,
        'weather': data['current_weather']
    }
    response = JsonResponse(response)

    search = Search.objects.filter(visitor_id=visitor_id, city=city, latitude=latitude, longitude=longitude).first()
    if search:
        search.count += 1
        search.last_search = datetime.now()
        search.save()
    else:
        Search.objects.create(visitor_id=visitor_id, city=city, latitude=latitude, longitude=longitude)

    if 'visitor_id' not in request.COOKIES:
        response.set_cookie('visitor_id', visitor_id, max_age=60*60*24*365*2)  # на 2 года, например

    return response


def last_searches(request):
    visitor_id = request.COOKIES.get('visitor_id')
    searches = Search.objects.filter(visitor_id=visitor_id).order_by('-last_search')[:5]

    cities = []
    for search in searches:
        cities.append({
            'city': search.city,
            'latitude': search.latitude,
            'longitude': search.longitude,
            'count': search.count
        })

    return JsonResponse(cities, safe=False)