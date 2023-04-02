from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

    def __str__(self) -> str:
        return self.name 


class Movie(models.Model):
    title = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name='genre', unique=False)
    numberInStock = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    dailyRentalRate = models.DecimalField( max_digits=3, decimal_places=2,
       validators=[
            MaxValueValidator(10),
            MinValueValidator(0)  
        ])
    publishDate = models.DateField(blank=True, null=True)
    liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title 
