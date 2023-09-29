from django.shortcuts import render
from django.http import HttpResponse
from .models import Home_videos,Services
# Create your views here.
def home(request):
    objects=Home_videos.objects.all()
    services =Services.objects.all()
    videos=[i.video.url for i in objects]
    services=[
        {
            'name':i.name,
            'image':i.image.url,
            'info':i.info,
        } for i in services
    ]
    
    return render(request, 'index.html', {'videos':videos,'services':services})
