from django import forms


from commets.models import Comment
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.Textarea)


    class Meta:

        model = Comment
        fields = ('user', 'profile', 'post', 'comment')