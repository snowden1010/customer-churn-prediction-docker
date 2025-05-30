import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    MODEL_PATH = os.environ.get('MODEL_PATH', 'models/model.pkl')
    DATA_PATH = os.environ.get('DATA_PATH', 'data/processed/processed_data.csv')
    DEBUG = os.environ.get('FLASK_DEBUG', False)

# You can add more configuration variables as needed
