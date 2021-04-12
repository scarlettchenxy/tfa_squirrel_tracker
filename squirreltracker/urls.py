from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('index', views.index, name='index'),
    path('squirrels_position', views.squirrels_position, name='squirrels_position'),
    path('squirrels/<str:unique_squirrel_id>', views.edit, name='squirrels'),
    path('squirrel', views.edit, name='edit'),
    path('squirrel/add', views.add, name='add'),
    path('squirrel/stats', views.stats, name='stats')
]
