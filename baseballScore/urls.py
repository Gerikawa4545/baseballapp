from django.urls import path, include
from baseballScore import views

urlpatterns = [
    path('', views.hello),
]
