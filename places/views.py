from django.shortcuts import render
from django.urls import reverse
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from places.models import PlaceName, Image


def serialize_post(post):
    post = {
        "title": post.title,
        "imgs": [
            pic.picture.url for pic in post.pics.all().order_by('numb')
        ],
        "description_short": post.short_description,
        "description_long": post.long_description,
        "coordinates": {
            "longitude": post.longitude,
            "latitude": post.latitude
        }
    }
    return post


def details_json(request, pk):
    post = get_object_or_404(PlaceName.objects.select_related(), pk=pk)
    post_data = serialize_post(post)
    return HttpResponse(JsonResponse(post_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4}), content_type="application/json")


def serialize_post2(post):
    redirect_url = reverse("details-json", args=[post.pk])

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post.longitude, post.latitude]
        },
        "properties": {
            "title": post.title,
            "detailsUrl": redirect_url
        }
    }


def index(request):
    posts = PlaceName.objects.all()
    context = {
        'places_posts': {"type": "FeatureCollection",
                         "features": [
                             serialize_post2(post) for post in posts
                         ]}
    }
    return render(request, 'index.html', context)
