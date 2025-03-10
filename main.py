from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import engine

from apps.item import routes as item_routes
from apps.item import models as item_models

from apps.user import routes as user_routes
from apps.user import models as user_models

from apps.auth import routes as auth_routes


item_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5500', 'http://127.0.0.1:5500'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {'message': 'This is root url'}


app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(item_routes.router)