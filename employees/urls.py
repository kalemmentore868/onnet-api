from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEmployee),
    path('post/', views.postEmployee)
]