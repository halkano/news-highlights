



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources= get_sources('general')


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
