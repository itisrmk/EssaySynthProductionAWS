from django import forms
from .models import CollegeEssay

class CollegeEssayForm(forms.ModelForm):
    class Meta:
        model = CollegeEssay
        fields = ['college_name', 'major', 'original_essay_title', 'original_essay_content']

        widgets = {
            'original_essay_content': forms.Textarea(attrs={'rows': 5}),
        }
        labels = { 
            'college_name': 'College Name',
            'major': 'Intended Major',
            'original_essay_title': 'Essay Title',
            'original_essay_content': 'Essay Content (Minimum 600 words)',
        }