from fastapi import FastAPI
from src.router import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(router)


origins = [
    "http://frontend:8082",
    "http://localhost:8082",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)