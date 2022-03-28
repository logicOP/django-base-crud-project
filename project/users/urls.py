from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='all'),
    path('users/<int:pk>/detail/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]

urlpatterns += [
    path('employees/create/', EmployeeCreateApi.as_view()),
    path('employees/list/', EmployeeApi.as_view()),
    path('employees/<int:pk>/update/', EmployeeUpdateApi.as_view()),
    path('employees/<int:pk>/delete/', EmployeeDeleteApi.as_view()),
]

urlpatterns += [
    path('employee/list/', employee_list()),
    path('employee/create/', create_employee()),
    path('employee/<int:pk>/details/', employee_details),
    path('employee/<int:pk>/update/', update_employee()),
    path('employee/<int:pk>/delete/', update_employee())
]
