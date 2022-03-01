import random
import string

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class CustomIDManager(models.Manager):

    def generate_unique_id(self):
        return ''.join(random.choices(string.digits, k=6))

    def create(self, *args, **kwargs):
        obj = None
        id = self.generate_unique_id()
        unique = False
        while not unique:
            try:
                obj = self.model(id=id, *args, **kwargs)
                obj.save()
                unique = True
            except IntegrityError:
                id = self.generate_unique_id()
        return obj


class GrantApplication(models.Model):
    EXPERIMENT_CHOICES = (
        ('Whole Genome Sequencing', 'Whole Genome Sequencing'),
        ('Metagenomics', 'Metagenomics'),
        ('Metatranscriptomics', 'Metatranscriptomics'),
        ('Transcriptomics (RNA Sequencing)', 'Transcriptomics (RNA Sequencing)'),
        ('Whole Exome Sequencing', 'Whole Exome Sequencing'),
        ('Small and long RNA sequencing', 'Small and long RNA sequencing'),
        ('Epigenetics', 'Epigenetics')
    )
    DNA_SOURCE_CHOICES = (
        ('Bacteria', 'Bacteria'), ('Human', 'Human'), ('Animals', 'Animals'),
        ('Plants', 'Plants'), ('Others', 'Others')
    )

    id = models.CharField(primary_key=True, max_length=6)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='grant_applications')
    title = models.CharField(max_length=500)
    description = models.TextField()
    nature_of_experiment = models.CharField(
        max_length=100, choices=EXPERIMENT_CHOICES)
    dna_source = models.CharField(max_length=50, choices=DNA_SOURCE_CHOICES)
    dna_source_others = models.CharField(max_length=100, null=True, blank=True)
    ipaddress = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    objects = CustomIDManager()