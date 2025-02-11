from contextlib import asynccontextmanager

from fastapi import FastAPI

from vkstarter.db import create_db, engine
from vkstarter.routers import create_note_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    '''Load the ML model.'''
    # Load the ML model
    create_db()
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(create_note_router(engine))
