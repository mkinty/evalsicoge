from django.urls import path
from .views import (
    results_view

)

app_name = 'results'

urlpatterns = [
    path('', results_view, name='result-view'),
]
