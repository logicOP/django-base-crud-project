from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', UserListView.as_view(), name='all'),
    path('users/<int:pk>/detail', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]

urlpatterns += [
    path('employee/create', EmployeeCreateApi.as_view()),
    path('employee/list', EmployeeApi.as_view()),
    path('employee/<int:pk>/update', EmployeeUpdateApi.as_view()),
    path('employee/<int:pk>/delete', EmployeeDeleteApi.as_view()),
]
