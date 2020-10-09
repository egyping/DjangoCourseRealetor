from django import forms

from .models import Unit, Comments


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]