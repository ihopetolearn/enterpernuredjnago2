from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .form import ArticleForm


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
    print(request)
    quiey_dict = request.GET
    try:
        quiry = int(quiey_dict.get('q'))
    except:
        quiry=None
    object = None
    if quiry is not None:
        object = Article.objects.get(id=quiry)
    context={
        "object":object,
    }
    return render(request,'articles/search.html',context=context)

def article_detail_view(request,id):
    # object = None
    if id is not None:
        object = Article.objects.get(id=id)
    context={
        "object":object,
        }


    return render(request,'articles/detail.html',context=context)
