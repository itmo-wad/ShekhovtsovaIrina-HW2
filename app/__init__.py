from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_login import LoginManager

server = Flask(__name__)
server.config.from_object(Config)
mongo = PyMongo(server)
login = LoginManager(server)

from app import routes,models