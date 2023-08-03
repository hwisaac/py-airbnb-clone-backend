from django.db import models

# Model 클래스를 상속한다
class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)