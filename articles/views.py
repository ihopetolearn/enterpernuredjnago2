from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .form import ArticleForm
from django.http import Http404
from django.db.models import Q


@login_required
def article_create_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article_object = form.save()  # Save the form data to create a new article object
            return redirect('home')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html',context=context)
# @login_required()
# def article_create_view(request):
#     form = ArticleForm()
#     context ={'form':form}
#     if request.method == "POST":
#         # print(request.POST)ls
#         form = ArticleForm(request.POST)
#         context['form']=form
#         if form.is_valid():
#             arif = form.cleaned_data.get("title")
#             paiman = form.cleaned_data.get("content")
#         if arif and paiman:
#          article_object=Article.objects.create(title=arif,content=paiman)
#         context['object'] = article_object
#         context['created'] = True
#     return render(request,'articles/create.html',context=context)

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.all()
    if query is not None:
        lookup = Q(title__icontains=query)
        qs = qs.filter(lookup)  # Use qs here instead of Article.objects
    context = {
        "key": qs,
    }
    return render(request, 'articles/search.html', context=context)
def article_detail_view(request,slug):
    obj_article = None
    if slug is not None:
        # obj_article = Article.objects.get(slug=slug)
        try:
            obj_article = Article.objects.get(id=slug)
        except Article.DoesNoteExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            obj_article = Article.objects.filter(slug=slug).first()
        except:
            pass
    context={
        "object":obj_article,
        }
    return render(request,'articles/detail.html',context=context)
