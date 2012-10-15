from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('main.api_views',

    # toss out any requests made to actual KA site urls
    url(r'^v1/', lambda x: HttpResponse("{}")),
    
    url(r'^save_video_log$', 'save_video_log'),
    url(r'^save_exercise_log$', 'save_exercise_log'),
    
)
