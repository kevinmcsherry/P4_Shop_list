from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopList, name='lists')
]