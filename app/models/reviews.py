class Review:

    all_reviews = []

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = imageurl
        self.publishedAt = publishedAt
        self.content = content


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

     @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.view_id == id:
                response.append(review)

        return response