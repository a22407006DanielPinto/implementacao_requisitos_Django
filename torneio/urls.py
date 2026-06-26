from django.urls import path
from . import views

urlpatterns=[
    path('', views.torneios_view, name='torneios_view'),
    path('atleta/<int:id>/', views.atletas_view, name='atletas_view'),
]