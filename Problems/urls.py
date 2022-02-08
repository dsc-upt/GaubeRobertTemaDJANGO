from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('problem/<slug:slug>', views.problem_page)
]