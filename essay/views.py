
from django.shortcuts import render, redirect
from .forms import CollegeEssayForm
from .models import CollegeEssay
from .mymodel import rewrite_mymodel
from .openAI import openai_response


def index(request):
    if request.method == 'POST':
        form = CollegeEssayForm(request.POST)
        if form.is_valid():
            essay = form.save(commit=False)

            rewritting_mymodel = rewrite_mymodel(essay.original_essay_content)
            essay.original_essay_content = openai_response(essay.college_name, essay.major, rewritting_mymodel, essay.original_essay_title)
            # essay.original_essay_content = openai_response(essay.college_name, essay.major, essay.original_essay_content, essay.original_essay_title)
            essay.original_essay_title = essay.original_essay_title
            essay.save()

            return render(request, 'essay/index.html', {'form': form, 'updated_essay': essay.original_essay_content, 'updated_title': essay.original_essay_title})
    else:
        form = CollegeEssayForm()
    return render(request, 'essay/index.html', {'form': form})

def faq(request):
    return render(request, 'essay/faq.html')

