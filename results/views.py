from django.shortcuts import render
from results.models import Result

# Create your views here.

def results_view(request):
    results = Result.objects.all()
    data = {}
    for res in results:
        res.questions = res.evaluation.get_questions()
        print(res.questions)
        for q in res.questions:
            q.answers = q.get_answers()
            data[q] = q.answers
            print(f"Question - Réponse : ${data.values()}" )
    context= {
        'results': results,

    }

    return render(request, 'results/result.html')