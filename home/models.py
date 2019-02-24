from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    show = models.CharField(max_length = 100)
    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 모음'

    def __str__(self):
        return self.title
# ../manage.py syncdb << run this file after modifyed model
