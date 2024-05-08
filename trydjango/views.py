import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string


# def home_view(request,*args,**kwargs):



def home(request):
    # Generating a random ID and fetching a random Article object
    random_id = random.randint(2, 4)  # Assuming 5 is the maximum ID
    random_article = Article.objects.get(pk=random_id)

    # Fetching all Article objects
    all_articles = Article.objects.all()

    # Constructing the context dictionary
    context = {
        "data": all_articles,  # Passing all Article objects
        "title": random_article.title,  # Passing title of the random Article
        "id": random_article.id,  # Passing ID of the random Article
        "content": random_article.content  # Passing content of the random Article
    }

    # Rendering the template with the context
    paiman = render_to_string('home_view.html', context=context)

    # Returning the rendered HTML content
    return HttpResponse(paiman)
