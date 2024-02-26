import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This-is-the-secret-key-ever@123321!!!'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/users'