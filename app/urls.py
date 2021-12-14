
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_music/', views.upload_music, name='upload_music'),
    path('deep_upload_music/', views.deep_upload_music, name='deep_upload_music'),
    path('search/', views.search, name='search'),
    path('base/', views.base, name='base'),
]