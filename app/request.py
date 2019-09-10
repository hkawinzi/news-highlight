import requests
from app.models import *
from config import Config

class getRequest:
    def __init__(self):
        self.api_key = Config.VIEW_API_KEY
    
    def get_sources(self,source):
        sources = []
        url_for_sources = 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(source, self.api_key)
        response = requests.get(url_for_sources).json()
        for data in response['sources']:
            sources.append(data)    
        print(sources)
        return sources
    
    def get_articles(self, article):
        articles = []
        url_for_articles = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article, self.api_key)
        response = requests.get(url_for_articles)
        for data in response.json()['articles']:
            articles.append(data)
        print(articles)
        return articles

    def get_articles_by_source(self):
        pass



