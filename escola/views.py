from django.shortcuts import render, get_object_or_404
from .models import Curso, Estudante

def escola_view(request):
    cursos = Curso.objects.all()
    return render(request, 'escola.html', {'cursos': cursos})

def estudante_view(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    return render(request, 'estudante.html', {'estudante': estudante})
