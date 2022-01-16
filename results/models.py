from django.db import models
from evaluations.models import Evaluation

# Create your models here.


class Result(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)