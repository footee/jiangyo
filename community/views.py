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

