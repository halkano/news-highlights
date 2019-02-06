from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
from ..request import get_articles
from ..models import Source,Article





    title = 'Home - TOP NEWS SOURCES'
    return render_template('index.html', title = title,sources= sources)

@main.route('/articles')
def articles():
    '''
    View  page function that returns the article1 page and its data
    '''

    # Getting headlines articles
    art = get_articles()

     #title = f'{Article.title}'
    return render_template('article.html',art = art)
