from django import forms
from learning_logs.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry

        # the field is the same with the attribute of class defined in the model
        fields = [
            'text', 
            # 'topic'
        ]
        labels = {
            'text': '',
            # 'topic': '',
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80})
        }
