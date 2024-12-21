from fastapi import BackgroundTasks, FastAPI
from .utils import logger
from .config import settings

app = FastAPI()

@app.get("/update")
async def update_db(background_task: BackgroundTasks):
    logger.info(f"{settings.aws_access_key_id}")
