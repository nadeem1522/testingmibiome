import random
import string

from django.db import models
from django.db.utils import IntegrityError


class CustomIDManager(models.Manager):

    def generate_unique_id(self):
        return 'MBQ' + ''.join(random.choices(string.digits, k=6))

    def create(self, *args, **kwargs):
        obj = None
        id = self.generate_unique_id()
        unique = False
        while not unique:
            try:
                obj = self.model(unique_id=id, *args, **kwargs)
                obj.save()
                unique = True
            except IntegrityError:
                id = self.generate_unique_id()
        return obj


class Quote(models.Model):
    unique_id = models.CharField(max_length=9, unique=True)
    sample_sub_attempts = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    project_name = models.CharField(max_length=500)
    project_use = models.CharField(max_length=30)
    study_nature = models.CharField(max_length=20)
    start_date = models.DateField()
    project_objective = models.TextField()
    project_outcome = models.TextField()
    service_choice = models.CharField(max_length=40)
    specific_service = models.CharField(max_length=100)
    customized_service = models.TextField(null=True, blank=True)
    ngs_platform = models.CharField(max_length=50)
    ngs_specify = models.CharField(max_length=100, null=True, blank=True)
    model_type = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=30)
    sample_type_specify = models.CharField(
        max_length=100, null=True, blank=True)
    prepared_library = models.CharField(max_length=500)
    sample_number = models.CharField(max_length=10)
    sequencing_parameter = models.CharField(max_length=40)
    sequencing_other = models.CharField(max_length=100, null=True, blank=True)
    sequencing_depth = models.CharField(max_length=50)
    expected_data = models.CharField(max_length=20)
    expected_data_specify = models.CharField(
        max_length=100, null=True, blank=True)
    reference_genome = models.CharField(max_length=500, null=True, blank=True)
    data_analysis = models.CharField(max_length=100)
    data_analysis_specify = models.CharField(
        max_length=100, null=True, blank=True)
    data_delivery = models.CharField(max_length=40)
    data_stored = models.CharField(max_length=10)
    comments = models.TextField(null=True, blank=True)
    hear_us = models.CharField(max_length=30, null=True, blank=True)
    hear_us_specify = models.CharField(
        max_length=100, null=True, blank=True)

    objects = CustomIDManager()