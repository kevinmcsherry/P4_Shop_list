from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, RemoveItem


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-item/', TaskCreate.as_view(), name='create-item'),
    path('edit-item/<int:pk>/', TaskUpdate.as_view(), name='edit-item'),
    path('remove-item/<int:pk>/', RemoveItem.as_view(), name='remove-item'),

]