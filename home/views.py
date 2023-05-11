from django.http import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {'amenities': Amenities.objects.all()}
    return render(request, 'index.html', context)

def get_hotel(request):
    try:
        hotel_objs = Hotel.objects.all()

        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                hotel_objs = hotel_objs.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                hotel_objs = hotel_objs.order_by('-hotel_price')
        if request.GET.get('amaount'):
            amaount = request.GET.get('amaount')
            hotel_objs = hotel_objs.filter(hotel_price__lte = amaount)
        if request.GET.get('amenities'):
            amenities = request.GET.get('amenities')
            amenities = str(amenities).split(',')
            am = []
            for amenity in amenities:
                am.append(int(amenity))
            hotel_objs = hotel_objs.filter(amenities__in = am).distinct()

        payload = []
        for hotel_obj in hotel_objs:
            payload.append({
                'hotel_name':hotel_obj.hotel_name,
                'hotel_price': hotel_obj.hotel_price,
                'hotel_desc': hotel_obj.hotel_desc,
                'banner_image': '/media/'+str(hotel_obj.banner_image),
                'amenities': hotel_obj.get_amenities()
            })
        print(hotel_obj.hotel_price)
        return JsonResponse(payload, safe=False)

    except Exception as e:
        print(e)
    return JsonResponse({'message':'Somthing went wrong'})

    