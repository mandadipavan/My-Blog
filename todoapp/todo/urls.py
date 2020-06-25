from django.urls import path
from . import views

urlpatterns=[
path('', views.TodoView, name='TodoView'),
path('update_list/<int:pk>/', views.UpdateList, name='update_list'),
path('delete_list/<int:pk>/', views.DeleteList, name='delete_list'),
]