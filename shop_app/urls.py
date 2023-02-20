from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-item/', TaskCreate.as_view(), name='create-item'),
    path('edit-item/<int:pk>/', TaskUpdate.as_view(), name='edit-item'),

]