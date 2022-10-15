from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='list'),
    path('create', views.CreateUser.as_view(), name='create'),
    path('login', views.Auth.as_view(), name='login'),
    path('logout', views.logout_request, name='logout'),
    path('<int:id>/edit', views.edit_user, name='edit'),
    path('<int:id>/update', views.update_user, name='update'),
    path('<int:id>/delete', views.delete_user, name='delete'),
]
