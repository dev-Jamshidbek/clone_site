from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name' , 'email' , 'body')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'id': 'id_email'}),
            'body': forms.Textarea(attrs={'id': 'id_body'}),
        }

