import os
import urllib.request,json
from .models import Source, Article

api_key = None

article_url = None

source_url = None
def configure_request(app):
    global api_key, article_url, source_url
    api_key = os.environ.get('NEWS_API_KEY')
    article_url = app.config['SOURCE_DATA_URL']
    source_url = app.config['SOURCE_URL']

def get_sources():

    with urllib.request.urlopen(source_url.format( api_key )) as url:
        response = json.loads(url.read())

        source_results = []

        if response['sources']:
            source_results = process_results(response['sources'])

    return source_results

def process_results(source_list):

    source_results = []

    for source_item in source_list:
        id=source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')
        category = source_item.get('category')

        source_result = Source(id, name, description, url , country , language, category)

        source_results.append(source_result)

    return source_results

def get_articles(title):

    with urllib.request.urlopen(article_url.format(title, api_key)) as url:

        article_details_response = json.loads(url.read())

        articles_result = []

        if article_details_response['articles']:
            article_object_list = article_details_response['articles']

    return articles_result


def process_articles(article_list):
    article_results = []

    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        article_result = Article(author, title, description. url, urlToImage, publishedAt, content)

        article_result.append(article_result)

        return article_results
