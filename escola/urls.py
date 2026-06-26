from django.urls import path
from . import views

urlpatterns=[
    path('', views.escola_view, name='escola_view'),
    path('estudante/<int:id>/', views.estudante_view, name='estudante_view'),
]