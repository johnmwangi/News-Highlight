from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,article_source,get_category,get_headlines

@main.route('/')
def index():

    # view root page function that returns the index page and its data

    # politicts_news = get_source('politics')
    # business_news = get_source('business')
    # sports_news = get_source('sports')
    # health_news = get_source('health')

    source= get_source()
    return render_template('index.html',sources=source, )


@main.route('/article/<id>')
def article(id):

    #title= 'article'

    articles = article_source(id)
    return render_template('article.html',articles = articles,id=id)

@main.route('/categories/<movie_name>')
def category(new_name):

    category = get_category(cat_name)
    title = f'{new_name}'
    new = new_name

    return render_template('categories.html',title=title,category = category, new= new_name)
