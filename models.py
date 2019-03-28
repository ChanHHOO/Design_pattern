from django.db import models


class Tese(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.title
# ../manage.py syncdb << run this file after modifyed model
