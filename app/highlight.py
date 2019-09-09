from flask import render_template
from app import app
from .request import get_views
from .request import get_views,get_view

@app.route('/')
def index():

    '''
    Highlight root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_views = get_views('popular')
    upcoming_view = get_views('upcoming')
    now_showing_view = get_views('now_playing')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_views, upcoming = upcoming_view, now_showing = now_showing_view )
#highlight
@app.route('/news/<int:view_id>')
def views(view_id):
    '''
    news root page function that returns the index page and its data
    '''
    # message = 'list and preview news articles from various sources.'
    views = get_movie(id)
    title = f'{views.title}'

    return render_template('news.html',title = title,views = views)
