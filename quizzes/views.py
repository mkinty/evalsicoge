from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Quiz
from .forms import QuizForm
# from quizzes.utils import generate_pdf


# Create your views here.

def result_view(request):
    results = Quiz.objects.all()
    query = request.GET.get('qs', '')
    if query:
        queryset = (Q(stage__icontains=query)) | (Q(name__icontains=query)) | (Q(stage_name__icontains=query)) | (
            Q(start_date__icontains=query)) | (Q(teacher__icontains=query))
        results = Quiz.objects.filter(queryset).distinct()
    # paginator = Paginator(questions, 20)
    # page_number = request.GET.get('page')
    # page_obj = Paginator.get_page(paginator, page_number)
    context = {
        # 'page_obj': page_obj,
        'results': results,
    }
    return render(request, 'quizzes/result.html', context)

def delete_result(request, pk):
    quiz = Quiz.objects.get(id=pk)
    if request.method == "POST":
        quiz.delete()
        return redirect('quizzes:result-view')
    context = {
        'quiz': owner,
    }
    return render(request, 'quizzes/delete.html', context)

def quiz_view(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quizzes:result-view')
    context = {
        'form': form,
    }
    return render(request, 'quizzes/quiz.html', context)

# def eval_view(request, pk):
#     """
#     student eval pdf views
#      """
#     eval = get_object_or_404(Quiz, id=pk)
#     other_formations = list(eval.other_formation2)
#
#     context = {
#         'other_formations': other_formations,
#         'eval': eval,
#     }
#     template_path = 'quizzes/eval.html'
#     pdf_name = 'Evaluation'
#     return generate_pdf(request, template_path, pdf_name, context)
