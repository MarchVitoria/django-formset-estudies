from django.shortcuts import render, redirect
from django.views import View
from articles.forms import ArticleForm
from django.forms import formset_factory
from django.urls import reverse

class ArticlesView(View):
    def get(self, request):
        ArticleFormSet = formset_factory(ArticleForm, extra=2)
        formset = ArticleFormSet()
        return render(request, 'articles.html', {'formset': formset})
    
    def post(self, request):
        ArticleFormSet = formset_factory(ArticleForm)
        formset = ArticleFormSet(request.POST)

        if formset.is_valid():
            print('VALIDOU O FORM')
            for form in formset:
                print(form.cleaned_data.get('title'))
                print(form.cleaned_data.get('discription'))
            return redirect('articles')
        print("NÃO VALIDOU O FORM")
        return render(request, 'articles.html', {'formset': formset})