from django import forms
from django.forms import ModelForm
from .models import Quiz


class DateInput(forms.DateInput):
    input_type = 'date'

class QuizForm(forms.ModelForm):
    EVAL_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    BOOL_CHOICES = (
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    )
    CHECK_CHOICES = (
        ('CSE', 'CSE'),
        ('SSCT', 'SSCT'),
        ('Référent harcèlement', 'Référent harcèlement'),
        ('Représentant de proximité', 'Représentant de proximité'),
        ('DUERP', 'DUERP'),
        ('AUTRES', 'AUTRES'),
    )
    TYPE_CHOICES = (
        ('Assistance juridique', 'Assistance juridique'),
        ('Communication / négociation', 'Communication / négociation'),
        ('Expertise SSCT', 'Expertise SSCT'),
        ('Expertise comptable', 'Expertise comptable'),
        ('Autres', 'Autres'),
    )
    FIND_CHOICES = (
        ('Site internet', 'Site internet'),
        ('Mailing', 'Mailing'),
        ('Entreprise ayant déjà participé à un stage SICOGE', 'Entreprise ayant déjà participé à un stage SICOGE'),
        ('Autre', 'Autre'),
    )
    # Organisation
    organization1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    organization2 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    organization3 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    # Formation
    formation1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    formation2 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    formation3 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    formation4 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    formation5 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    formation6 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    # Formateur(s)
    teacher1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    teacher2 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    teacher3 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    teacher4 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    # Appréciation générale
    appreciation1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    appreciation2 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=EVAL_CHOICES,
    )
    # Recommandation de la formamtion
    recommendation1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=BOOL_CHOICES,
    )
    # Autres besoins de la formation
    other_formation1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=BOOL_CHOICES,
    )
    other_formation2 = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHECK_CHOICES,
    )
    # Types, autres besoins de la formation
    other_formation_type1 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=BOOL_CHOICES,
    )
    other_formation_type2 = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE_CHOICES,
    )
    # Comment avez-vous connu ce stage
    find = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FIND_CHOICES,
    )
    class Meta:
        model = Quiz
        fields = '__all__'
        widgets = {
            'start_date': DateInput(attrs={'type': 'text'}),
            'end_date': DateInput(attrs={'type': 'text'}),
            'election_date': DateInput(attrs={'type': 'text'}),
            'stage': forms.RadioSelect,
        }
