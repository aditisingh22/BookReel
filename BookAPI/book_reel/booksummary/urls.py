from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name ="index"),
    path('/accounts/profile', views.profile,name = "profile")
]
