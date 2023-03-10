from django import forms
from django.forms import TextInput

from .models import PhotoPost, Comment
from django import forms
# from .views import *


class PhotoPostForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False, label='Прикрепить изображения')

    class Meta:
        model = PhotoPost
        fields = ['title', 'description', 'image']


class UploadPostsForm(forms.Form):
    file = forms.ImageField()


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('post_comment', 'user', 'likes')
