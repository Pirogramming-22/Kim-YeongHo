from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField('이름' , max_length=30)
    category = models.CharField('종류' , max_length=20)
    explanation = models.TextField('설명')

    def __str__(self):
        return self.name