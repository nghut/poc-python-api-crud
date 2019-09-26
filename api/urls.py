from django.urls import path

from . import views

urlpatterns = [
    path('/create', views.create, name='Create'),
    path('/read', views.read, name='Read'),
    path('/update', views.update, name='Read'),
    path('/delete', views.delete, name='Read'),
]