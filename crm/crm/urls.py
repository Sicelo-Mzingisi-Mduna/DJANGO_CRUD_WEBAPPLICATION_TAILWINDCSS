
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Custom url for the web application
    path('', include('webapp.urls')),
    
    #django browser reload for live reloading
    path("__reload__/", include("django_browser_reload.urls")),
]
