"""用于添加主题的表单"""
from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
