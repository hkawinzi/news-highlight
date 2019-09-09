class View:
    '''
    News view class to define News Objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = 'https://cointelegraph.com/news/crypto-and-blockchain-adoption-grows-5-important-developments-sept-28'
        self.urlToImage = 'https://images.cointelegraph.com/images/740_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS9zdG9yYWdlL3VwbG9hZHMvdmlldy8wMzYyZDU2NTQxN2JjNmY0ZmQyMzk0MGM0Y2VmYTlkNC5qcGc=.jpg'
        self.publishedAt = publishedAt
        self.content = content