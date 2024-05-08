from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']


    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qv = Article.objects.all().filter(title__icontains=title)
        if qv.exists():
            self.add_error("title",f"{title}  is already in use tryanother word")
        return data




class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def cleaned_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('this is already token')
    #     return title


    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         raise forms.ValidationError('indentation is very crucial in the python this title is teken')
    #     content = cleaned_data.get('content')
    #     if "offic" in title.lower() or "office "in content:
    #         self.add_error('content','office can not be in the contenet ')
    #         raise forms.ValidationError('thsi is not allowed ')
    #     return cleaned_data



