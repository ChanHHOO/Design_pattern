from django.forms imoprt ModelForm
from .models import Home

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ['name', 'email', 'show']
