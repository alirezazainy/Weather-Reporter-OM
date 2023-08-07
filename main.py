from fastapi import FastAPI
from DB.models import Base
from DB.database import engine
from fastapi.middleware.cors import CORSMiddleware
from Routers.reports import router

# Generate API instance
app = FastAPI(title="Open-Meteo Reporter",
               description="an API to Save Open Meteo Information of Locations")
# Generate Database 
Base.metadata.create_all(engine)
# Add Routers 
app.include_router(router)
# Include CORS middleware
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
    """
    Wellcome
    """
    return "Wellcome to Weather Reporter of Open Meteo"


# Coded With Galb:)