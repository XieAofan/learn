from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='my_login'),
    path('q/', views.q, name='q'),
    path('logout/', views.my_logout, name='my_logout'),
]