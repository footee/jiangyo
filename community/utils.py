
# Create your views here.


from community.models import CommunityInfo, CommunityPrice
import math




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


def analysis():
    CommunityPrice  
    
    

