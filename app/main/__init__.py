import os
from flask import Flask
from .config import DevConfig
import bootstrap
from app import highlight
from app import error

#initializing application
app = Flask(__name__,instance_relative_config= True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import highlight