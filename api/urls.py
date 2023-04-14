from django.urls import path

from . import views

urlpatterns = [
    path("get_question", views.get_question, name="gp"),
    path("add_question", views.add_question, name="ap"),
]