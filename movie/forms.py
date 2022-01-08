from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'image', 'description','actor1','actor2','actor3','cat']