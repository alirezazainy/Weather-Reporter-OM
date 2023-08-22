from fastapi import FastAPI, Security
from DB.models import Base
from DB.database import engine
from fastapi.middleware.cors import CORSMiddleware
from Routers import reports, responses
from authorization import get_current_user
from schemas import UserBase
# Generate API instance

app = FastAPI(title="Open-Meteo Reporter",
               description="an API to Save Open Meteo Information of Locations")
# Generate Database 
Base.metadata.create_all(engine)
# Add Routers 
app.include_router(reports.router)
app.include_router(responses.router)
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
    return "Wellcome to Weather Reporter of Open Meteo\n Tip: for use this service please authenticate at https://admin.samacontrol.com/#/auth/login"


# Coded With Galb:)