from django import forms

class QuestionForm(forms.Form):
    question_field = forms.CharField(label='Question', widget=forms.TextInput(attrs={'placeholder': 'Enter your question to know your fate...'}))