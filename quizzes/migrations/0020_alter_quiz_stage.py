# Generated by Django 3.2.8 on 2021-12-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0019_alter_quiz_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='stage',
            field=models.CharField(blank=True, choices=[('Présentiel', 'Présentiel'), ('Visio', 'Visio')], max_length=200, null=True),
        ),
    ]
