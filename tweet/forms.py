from django import forms


class TweetPostForm(forms.Form):
    content = forms.CharField(label="tweet", max_length=50)
