from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import JSONResponse
from .utils import logger
from .config import settings
from gnews import GNews

app = FastAPI()
google_news = GNews()

@app.get("/search/{keyword}")
async def search_news(keyword: str):
    logger.info(f"Searching news for keyword: {keyword}")
    
    # Fetch news using GNews
    content = google_news.get_news(keyword)
    print(content)
    
    
    return content