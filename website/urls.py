from django.urls import path
from . import views

urlpatterns = [
    path('/cadastro', views.cadastro, name="cadastro.html"),
    path('', views.index, name="index.html"),
    path('/produtos', views.index, name="index.html")
]