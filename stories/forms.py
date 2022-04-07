from django import forms
# from .widgets import CustomClearableFileInput
from .models import Stories, Comment


class StoryForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = '__all__'

    image_before = forms.ImageField(label='Image',
                        required=False)
                        # widget=CustomClearableFileInput)
                        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)