from gnews import GNews
from .base import NewsFetcher


class GNewsFetcher(NewsFetcher):
    def __init__(self):
        self.gnews = GNews()

    def fetch(self, keyword: str) -> list:
        results = self.gnews.get_news(keyword)
        
        return results
    


a = GNewsFetcher()
r = a.fetch('hnb')
print(r)