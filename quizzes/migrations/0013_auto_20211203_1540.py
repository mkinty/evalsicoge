# Generated by Django 3.2.8 on 2021-12-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0012_auto_20211203_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='company_activity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='election_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='find',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='find_comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='function',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='other_formation_comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='other_formation_type_comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='total_company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='total_establishment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
