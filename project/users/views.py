from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User


class UserBaseView(View):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('users:all')


class UserListView(UserBaseView, ListView):
    """View to list all Users.
    Use the 'User_list' variable in the template
    to access all User objects"""


class UserDetailView(UserBaseView, DetailView):
    """View to list the details from one User.
    Use the 'User' variable in the template to access
    the specific User here and in the Views below"""


class UserCreateView(UserBaseView, CreateView):
    """View to create a new User"""


class UserUpdateView(UserBaseView, UpdateView):
    """View to update a User"""


class UserDeleteView(UserBaseView, DeleteView):
    """View to delete a User"""
