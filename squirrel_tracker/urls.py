from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('map/', include('map.urls')),
    path('sightings/', include('sightings.urls')),
    path('admin/', admin.site.urls),
]

