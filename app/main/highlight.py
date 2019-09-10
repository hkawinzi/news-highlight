from flask import render_template,request,redirect,url_for
from . import main 
from app.request import getRequest

rqst = getRequest()

@main.route('/')
def index():
    '''
    Highlight root page function that returns the index page and its data
    '''
    sources = rqst.get_sources('tech')
    if sources:
        return render_template("index.html", sources=sources)   


@main.route('/view/<int:view_id>')
def view(id):
    '''
    news root page function that returns the index page and its data
    '''
