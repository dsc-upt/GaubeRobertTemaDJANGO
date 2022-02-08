from django.shortcuts import render

# Create your views here.

problems = [
    'prima_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob', '2_prob', '3_prob'
]

def index(request):
    return render(request, 'Problems/index.html', {
        'problems': problems
    })

def problem_page(request, slug):
    return render(request, 'Problems/problem_page.html', {
        'title': slug
    })