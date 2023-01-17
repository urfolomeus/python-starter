from fastapi import FastAPI

from .api import ping

app = FastAPI(title="Python Starter", version="0.1.0")

app.include_router(ping.router)
