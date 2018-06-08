from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('products/<slug>', views.match_detail, name='match_detail'),
]

