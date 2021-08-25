from django.shortcuts import render
from django.http import HttpResponse
import random

from .forms import QuestionForm


def index(request):  
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        answers = {
            "1": "Definetely Yes",
            "2": "Yes",
            "3": "Maybe",
            "4": "Ask later",
            "5": "No",
            "6": "Definetely No",
            "7": "The answer is not clear"
        }
        answer = random.choice(list(answers.values()))
    else:
        form = QuestionForm()
        answer = ''
    return render(request, 'magic/home.html', {'form': form, 'answer': answer})