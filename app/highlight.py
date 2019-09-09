from flask import render_template,request,redirect,url_for
from app import app
from .request import get_views
from .request import get_views,get_view,search_view
from .models import review
from .forms import ReviewForm

Review = review.Review

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
    search_view = request.args.get('news_query')

    if search_view:
        return redirect(url_for('search',view_name=search_view))
    else:
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
@app.route('/search/<movie_name>')
def search(view_name):
    '''
    View function to display the search results
    '''
    view_name_list = view_name.split(" ")
    view_name_format = "+".join(view_name_list)
    searched_views = search_view(view_name_format)
    title = f'search results for {view_name}'
    return render_template('search.html',views = searched_views)

@app.route('/view/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    view = get_view(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(view.author,title,description,url,urlToImage,publishedAt,content)
        new_review.save_review()
        return redirect(url_for('view',id = view.id ))

    title = f'{view.title} review'
    return render_template('new_review.html',title = title, review_form=form, view=view)

@app.route('/view/<int:id>')
def view(id):

    '''
    View view page function that returns the view details page and its data
    '''
    view = get_view(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(view.id)

    return render_template('news.html',title = title,view = view,reviews = reviews)