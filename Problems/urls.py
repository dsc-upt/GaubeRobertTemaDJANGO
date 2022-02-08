from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('problem/<int:id>', views.problem_page)
]