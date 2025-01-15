from django.db import models
from DevTool.models import Devtool

# Create your models here.
class Post(models.Model):
    title = models.CharField('아이디어 이름' , max_length=20)
    image = models.ImageField('사진' , upload_to='blog/%Y%m%d' , blank=True)
    explanation = models.TextField('설명')
    interest = models.IntegerField('관심도')
    expectedTool = models.ForeignKey(Devtool , verbose_name='개발툴', on_delete=models.CASCADE)
    created_at = models.DateTimeField('생성시간',auto_now_add=True)
    star = models.BooleanField("찜 여부", default=False)

    def __str__(self):
        return self.title