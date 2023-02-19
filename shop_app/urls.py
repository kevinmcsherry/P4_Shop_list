from django.urls import path
from .views import shopList


urlpatterns = [
    path('', shopList.as_view(), name='lists')
]