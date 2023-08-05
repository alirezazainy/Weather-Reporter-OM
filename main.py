from fastapi import FastAPI
from DB.models import Base
from DB.database import engine
from fastapi.middleware.cors import CORSMiddleware
from Routers.reports import router


app = FastAPI(title="Open-Meteo Reporter",
               description="an API to Save Open Meteo Information of Locations")
Base.metadata.create_all(engine)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
        "https://localhost"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return "Wellcome to Weather Reporter of Open Meteo"


# Coded With Galb:)