import os

class Config:
    '''
    General confirguration parent class
    '''

    NEWS_API_BASE_URL="https://newsapi.org/v2/{}?country=us&apiKey={}"
    # NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY='b283063849aa43109644ce46915578fd'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}