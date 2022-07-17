from django.urls import path
# internal imports
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
