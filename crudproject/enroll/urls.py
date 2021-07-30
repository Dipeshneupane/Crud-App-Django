from django.urls import path
from .views import *

urlpatterns = [
    path("", addShow, name = "addShow"),
    path('delete/<int:id>/', deleteData, name = "deleteData"),
    path("<int:id>", updateData, name = 'updateData'),
]
