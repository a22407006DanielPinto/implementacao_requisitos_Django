from django.urls import path
from . import views

urlpatterns=[
    path('', views.receitas_view, name='receitas_view'),
    path('utilizador/<int:id>/', view.utilizadores_view, name='utilizadores_view'),
]