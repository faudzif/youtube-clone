import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")


app = FastAPI()

app.add_middleware(CORSMiddleware, origins=origins)

