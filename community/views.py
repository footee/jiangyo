# Create your views here.


from community.models import CommunityInfo, CommunityPrice
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Context, Template
from django.utils.http import urlquote
from django.conf import settings
from django.utils import simplejson



def googlemap(request):
    return render_to_response('index.html')


def community(request):

    community = CommunityInfo.objects.exlude(latitude=NULL).exlude(longtitude=NULL).defer("longitude", "latitude", "name")

    content = simplejson.dumps(community)

    print("community view")
    return HttpResponse(content)
