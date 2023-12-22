from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=80)
    discription = forms.CharField(max_length=300)