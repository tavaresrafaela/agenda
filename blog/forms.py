from django import forms
from .models import Post
from .models import Cadastro

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CadForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ('nome', 'idade', 'email', 'telefone', 'aniversario',)