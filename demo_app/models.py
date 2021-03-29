from django.db import models

# Create your models here.
class ExampleModel(models.Model):

    name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)