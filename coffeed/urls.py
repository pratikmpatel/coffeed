from django.conf.urls import include, url
from django.contrib import admin
import core.views as coreviews

urlpatterns = [




    url(r'^admin/', admin.site.urls),
    url(r'^$', coreviews.SplashView.as_view()),	
    	]
