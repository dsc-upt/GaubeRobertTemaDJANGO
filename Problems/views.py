from django.shortcuts import render, get_object_or_404
from .models import Problem
from django.views import View
from django.http import HttpResponseRedirect
from .test_source import main
import os

# Create your views here.

def save_file(file):
    with open("files/source.cpp", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

def index(request):
    problems = Problem.objects.all().order_by("rating")
    return render(request, 'Problems/index.html', {
        'problems': problems
    })

class ProblemPage(View):
    def get(self, request, id):
        problem = get_object_or_404(Problem, pk=id)
        return render(request, 'Problems/problem_page.html', {
            'problem': problem
        })

    def post(self, request, id):
        save_file(request.FILES['source'])
        problem = get_object_or_404(Problem, pk=id) 
        answers = main(problem.test_data_in.url, problem.test_data_out.url)

        if answers[0]['index'] == -1:
            text = "Compilare nereusita"
            return render(request, "Problems/problem_page.html", {
                'problem': problem,
                'text': text
            })
        else:
            return render(request, "Problems/answers.html", {
                'answers': answers  
            })