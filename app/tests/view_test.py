import unittest
from app.models import view


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_view = View('Cointelegraph By Aaron Wood','Crypto and Blockchain Adoption Grows: 5 Important Developments Sept. 2–8','Adoption is critical for the success of the blockchain and cryptocurrency industries. Here are five examples of developments that could spur adoption from last week','https://cointelegraph.com/news/crypto-and-blockchain-adoption-grows-5-important-developments-sept-28','https://images.cointelegraph.com/images/740_aHR0cHM6Ly9zMy5jb2ludGVsZWdyYXBoLmNvbS9zdG9yYWdlL3VwbG9hZHMvdmlldy8wMzYyZDU2NTQxN2JjNmY0ZmQyMzk0MGM0Y2VmYTlkNC5qcGc=.jpg','2019-09-09T01:49:00Z','Analysts have long predicted that the increased participation of governments and institutional players in the blockchain and cryptocurrency space shows how the respective industries are maturing. The founder of crypto merchant bank Galaxy Digital, Michael Nov… [+3146 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_view,View))

if __name__ == '__main__':
    unittest.main()


