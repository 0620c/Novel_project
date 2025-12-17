from fastapi import FastAPI
from app.api import router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Webtoon ML Pipeline")
app.include_router(router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")