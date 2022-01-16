from django.db import models

class Quiz(models.Model):
    # En tête
    FV_CHOICES = (
        ('Présentiel', 'Présentiel'),
        ('Visio', 'Visio'),
    )
    stage = models.CharField(choices=FV_CHOICES, max_length=200, null = True, blank = True)
    stage_name = models.CharField(max_length=200, null = True, blank = True)
    start_date = models.DateField(max_length=200, null = True, blank = True)
    end_date = models.DateField(max_length=200, null = True, blank = True)
    place = models.CharField(max_length=200, null = True, blank = True)
    teacher = models.CharField(max_length=200, null = True, blank = True)
    # Organisation
    organization1 = models.CharField(max_length=200, null = True, blank = True)
    org_comment1 = models.CharField(max_length=200, null = True, blank = True)
    organization2 = models.CharField(max_length=200, null = True, blank = True)
    org_comment2 = models.CharField(max_length=200, null = True, blank = True)
    organization3 = models.CharField(max_length=200, null = True, blank = True)
    org_comment3 = models.CharField(max_length=200, null=True, blank=True)
    # Formation
    formation1 = models.CharField(max_length=200, null = True, blank = True)
    for_comment1 = models.CharField(max_length=200, null=True, blank=True)
    formation2 = models.CharField(max_length=200, null = True, blank = True)
    for_comment2 = models.CharField(max_length=200, null=True, blank=True)
    formation3 = models.CharField(max_length=200, null = True, blank = True)
    for_comment3 = models.CharField(max_length=200, null=True, blank=True)
    formation4 = models.CharField(max_length=200, null = True, blank = True)
    for_comment4 = models.CharField(max_length=200, null=True, blank=True)
    formation5 = models.CharField(max_length=200, null = True, blank = True)
    for_comment5 = models.CharField(max_length=200, null=True, blank=True)
    formation6 = models.CharField(max_length=200, null = True, blank = True)
    for_comment6 = models.CharField(max_length=200, null=True, blank=True)
    # Formateur(s)
    teacher1 = models.CharField(max_length=200, null = True, blank = True)
    tea_comment1 = models.CharField(max_length=200, null=True, blank=True)
    teacher2 = models.CharField(max_length=200, null = True, blank = True)
    tea_comment2 = models.CharField(max_length=200, null=True, blank=True)
    teacher3 = models.CharField(max_length=200, null = True, blank = True)
    tea_comment3 = models.CharField(max_length=200, null=True, blank=True)
    teacher4 = models.CharField(max_length=200, null = True, blank = True)
    tea_comment4 = models.CharField(max_length=200, null=True, blank=True)
    # Appréciation générale
    appreciation1 = models.CharField(max_length=200, null = True, blank = True)
    ap_comment1 = models.CharField(max_length=200, null=True, blank=True)
    appreciation2 = models.CharField(max_length=200, null = True, blank = True)
    ap_comment2 = models.CharField(max_length=200, null=True, blank=True)
    # Recommandation de la formamtion
    recommendation1 = models.CharField(max_length=200, null = True, blank = True)
    recommendation2 = models.CharField(max_length=200, null = True, blank = True)
    # Autres besoins de la formation
    other_formation1 = models.CharField(max_length=200, null=True, blank=True)
    other_formation2 = models.CharField( max_length=200, null = True, blank = True)
    other_formation_comment = models.CharField(max_length=200, null=True, blank=True)
    # Types, autres besoins de la formation
    other_formation_type1 = models.CharField(max_length=200, null=True, blank=True)
    other_formation_type2 = models.CharField( max_length=200, null = True, blank = True)
    other_formation_type_comment = models.CharField(max_length=200, null = True, blank = True)
    # PARTICIPANT
    name = models.CharField(max_length=200, null=True, blank=True)
    function = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    company_activity = models.CharField(max_length=200, null=True, blank=True)
    total_company = models.CharField(max_length=200, null=True, blank=True)
    total_establishment = models.CharField(max_length=200, null=True, blank=True)
    election_date = models.DateField(max_length=200, null = True, blank = True)
    # Comment avez-vous connu ce stage
    find = models.CharField( max_length=200, null=True, blank=True)
    find_comment = models.CharField(max_length=200, null=True, blank=True)
    # created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
