from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    test_data_in = models.FileField(upload_to="files/test_data_in")
    test_data_out = models.FileField(upload_to="files/test_data_out")
    
    def get_url(self):
        return reverse("problem", args=[self.slug])
