from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("addShow", addShow, name = "addShow"),
    path('delete/<int:id>/', deleteData, name = "deleteData"),
    path("<int:id>", updateData, name = 'updateData'),
    path('', LoginView.as_view(), name = 'login'),
    path('register', Register, name = 'register'),
]
