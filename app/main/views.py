from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Source, Article

@main.route('/', methods=['GET','POST'])
def index():
    sources = get_sources()
    # general = get_sources('general')
    # entertainment = get_sources('entertainment')
    # sports = get_sources('sports')
    # technology = get_sources('technology')
    # science = get_sources('science')
    # health = get_sources('health')

    title = 'News Highlights'

    return render_template('base.html', title = title, sources = sources)


@main.route('/sources/<title>', methods=['GET','POST'])
def articles(title):
    articles = get_articles(title)

    return render_template('articles.html', articles = articles)

