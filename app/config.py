class Config:
    '''
    General configuration parent class
    '''
    VIEW_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&from=2019-08-09&sortBy=publishedAt&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True