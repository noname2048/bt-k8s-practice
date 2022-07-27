"""
main.py for run fastapi
"""
from datetime import timezone, timedelta, datetime

from fastapi import FastAPI

import uvicorn

KST = timezone(timedelta(hours=9))
PRETTY_TIME_FORMAT = "%y년%m월%d일, %H시%M분%S초"
app = FastAPI()


@app.get("/")
async def index():
    """
    Health check api for index

    return string format server time
    """
    now: datetime = datetime.now(tz=KST)
    str_time: str = now.strftime(PRETTY_TIME_FORMAT)
    return {"message": str_time, "company": "알고리마"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
