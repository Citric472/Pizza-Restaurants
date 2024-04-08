import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management (change this to something unique and secret)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'

    # Debug mode (set to True for development, False for production)
    DEBUG = True
