from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate
from .views import TaskUpdate, RemoveItem, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-item/', TaskCreate.as_view(), name='create-item'),
    path('edit-item/<int:pk>/', TaskUpdate.as_view(), name='edit-item'),
    path('remove-item/<int:pk>/', RemoveItem.as_view(), name='remove-item')
]
