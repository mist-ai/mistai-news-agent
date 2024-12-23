from .base import Analyzer
from transformers import pipeline


class FinbertAnalyzer(Analyzer):
    def __init__(self):
        """
        Initializes the FinbertAnalyzer with the ProsusAI FinBERT model for sentiment analysis.
        """
        self.sentiment_analyzer = pipeline("text-classification", model="ProsusAI/finbert")

    def analyze(self, articles):
        """
        Analyzes the sentiment of a list of articles.

        Args:
            articles (List[Dict[str, str]]): 
                A list of dictionaries representing articles. Each dictionary should have a "content" key.

        Returns:
            List[Dict[str, Any]]: 
                A list of dictionaries where each dictionary contains the original article data 
                along with its sentiment score and label.
        """
        analyzed_articles = []
        for article in articles:
            content= article['content']
            if content:
                sentiment = self.sentiment_analyzer(content)[0] 
                article["sentiment_label"] = sentiment["label"]
                article["sentiment_score"] = sentiment["score"]
            else:
                
                article["sentiment_label"] = None
                article["sentiment_score"] = None
            
            break

        return analyzed_articles


a = FinbertAnalyzer()
print(a.analyze([{"content": "Sri Lanka’s HNB profits up 262-pct in June quarter",
  "model": "Mustang",
  "year": 1964}]))