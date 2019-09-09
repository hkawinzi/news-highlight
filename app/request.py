from app import app
import urllib.request,json
from .models import view

View = view.View

#getting api key
api_key = app.config['VIEW_API_KEY']

#getting the view base url
base_url = app.config["VIEW_API_BASE_URL"]

def get_views (category):
    '''
    Function that gets the json response to our url request
    '''
    get_views_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_views_url) as url:
        get_views_data = url.read()
        get_views_response = json.loads(get_views_data)

        view_results = None

        if get_views_response['results']:
            view_results_list = get_views_response['results']
            view_results = process_results(view_results_list)

def process_results(view_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        view_list: A list of dictionaries that contain news details

    Returns :
        view_results: A list of news objects
    '''
    view_results = []
    for view_item in view_list:
        author = view_item.get('author')
        title = view_item.get('original_title')
        description = view_item.get('description')
        url = view_item.get('url_path')
        urlToImage = view_item.get('urlToImage')
        publishedAt = view_item.get('publishedAt')
        content = view_item.get('content')


        if url:
            view_object = View(author,title,description,url,urlToImage,publishedAt,content)
            view_results.append(view_object)

def get_view(id):
    get_view_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_view_details_url) as url:
        view_details_data = url.read()
        view_details_response = json.loads(view_details_data)

        view_object = None
        if view_details_response:
        author = view_item.get('author')
        title = view_item.get('original_title')
        description = view_item.get('description')
        url = view_item.get('url_path')
        urlToImage = view_item.get('urlToImage')
        publishedAt = view_item.get('publishedAt')
        content = view_item.get('content')

            view_object = View(author,title,description,url,urlToImage,publishedAt,content)

    return movie_object

