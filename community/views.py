# Create your views here.


from community.models import CommunityInfo, CommunityPrice
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Context, Template
from django.utils.http import urlquote
from django.conf import settings
import json
import math



def googlemap(request):
    return render_to_response('index.html')


def community(request):
    communities = CommunityInfo.objects.filter(latitude__isnull=False).only("name", "latitude", "longitude")

    array = {}
    for c in communities:
        array[c.name] = {"la":c.latitude, "lo":c.longitude}

    data = json.dumps(array)
    print(data)

    return HttpResponse(data)


def distance(lat1, lng1, lat2, lng2):
    earth_radius = 6378137 # unit: meter
    radLat1 = math.radians(lat1)
    radLat2 = math.radians(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) +
        math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
    s = s * earth_radius
    s = math.round(s * 100) / 100
    return s

