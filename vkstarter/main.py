from contextlib import asynccontextmanager

from fastapi import FastAPI

from vkstarter.db import create_db
from vkstarter.routers import note


@asynccontextmanager
async def lifespan(app: FastAPI):
    '''Load the ML model.'''
    # Load the ML model
    create_db()
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(note)
