# from django import forms
# from .models import Stories, Comment


# class StoryForm(forms.ModelForm):
#     class Meta:
#         model = Stories
#         fields = '__all__'
    
#     image = forms.ImageField(label='Image',
#                         required=False


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         categories = Category.objects.all()
#         friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

#         self.fields['category'].choices = friendly_names
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'border-black rounded-0'
    
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body',)