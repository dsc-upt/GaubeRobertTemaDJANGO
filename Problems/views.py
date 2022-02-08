from django.shortcuts import render, get_object_or_404
from .models import Problem

# Create your views here.

def index(request):
    problems = Problem.objects.all().order_by("rating")
    return render(request, 'Problems/index.html', {
        'problems': problems
    })

def problem_page(request, id):
    problem = get_object_or_404(Problem, pk=id)
    return render(request, 'Problems/problem_page.html', {
        'problem': problem
    })