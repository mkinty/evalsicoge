from django.urls import path
from .views import (
    quiz_view,
    eval_view,
    result_view,
    delete_result
)

app_name = 'quizzes'

urlpatterns = [
    path('', quiz_view, name='quiz-view'),
    path('results/', result_view, name='result-view'),
    path("results/delete/<str:pk>/", delete_result, name='delete-quiz'),
    path("eval/<str:pk>/", eval_view, name='eval-view'),
]
