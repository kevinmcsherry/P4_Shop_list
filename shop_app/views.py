from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import login
from .models import Task


# Create your views here.

class Login(SuccessMessageMixin, LoginView):
    template_name = 'shop_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Login Successful"
    
    def get_success_url(self):
        return reverse_lazy('tasks')
        

class CreateAccount(SuccessMessageMixin, FormView):
    template_name = 'shop_app/create_account.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_message = "Account Created Successfully"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateAccount, self).form_valid(form)

    def state(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(CreateAccount, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('Search-field') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__istartswith=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'shop_app/shop_list.html'


class TaskCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_message = "Item Added Successfully"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_message = "Item updated successfully"
    success_url = reverse_lazy('tasks')


class RemoveItem(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Task
    success_message = "Item Removed Successfully"
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
