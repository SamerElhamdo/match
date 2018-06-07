from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('<slug>', views.match_list_by_lig, name='match_list_by_lig'),
    path('products/<slug>', views.match_detail, name='match_detail'),
]

