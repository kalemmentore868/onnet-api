from django.urls import path
from . import views

urlpatterns = [
    path('', views.getClient),
    path('post/', views.postClient)
]