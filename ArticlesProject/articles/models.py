from django.db import models
from django.utils import timezone

class ArticlesModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    discription = models.CharField(max_length=300)
    pub_date = models.DateTimeField(timezone.now())