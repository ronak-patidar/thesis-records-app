from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
class  Phdtable(models.Model):
    student_name=models.CharField(max_length=100)
    supervisor_name=models.CharField(max_length=100)
    thesis_title=models.CharField(max_length=300)
    submission_year=models.IntegerField()
    department=models.CharField(max_length=100)
    