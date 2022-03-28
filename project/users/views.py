from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import EmployeeForm
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.shortcuts import render
from .models import User, Employee

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import EmployeeSerializer


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


# Crud using REST Framework
class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect('/employee/list/')


def employee_list(request):
    data = {"dataset": Employee.objects.all()}
    return render(request, "employees/list_employee.html", data)


def employee_details(request, employee_id):
    context = {"data": Employee.objects.get(id=employee_id)}
    return render(request, "employees/details_employee.html", context)


def update_employee(request, employee_id):
    context = {}

    obj = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/employee/' + str(employee_id) + '/details/', employee_details)

    context["form"] = form

    return render(request, "employees/update_employee.html", context)


def delete_employee(request, employee_id):
    context = {}

    obj = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/employee/list/")

    return render(request, "employees/delete_employee.html", context)
