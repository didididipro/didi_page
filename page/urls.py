from django.urls import path, include
from .views import PageView

urlpatterns = [
    path("", PageView.as_view(), name="home"),
]
