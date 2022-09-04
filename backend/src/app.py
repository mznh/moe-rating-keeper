#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import api

app = FastAPI()
# for cors setting
origins = [
    "http://localhost:4200",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)
app.include_router(api.player.api)
app.include_router(api.battle.api)
app.include_router(api.rating.api)

@app.get("/")
async def root():
    return {"message": "This is MoE Rating Keeper Api Server"}

