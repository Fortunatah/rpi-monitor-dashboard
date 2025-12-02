## /backend/api
## this will use fastAPI to use build an API communicate with the front end

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metrics import get_system_metrics  ## from /backend/metrics.py
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

## Build the app

app = FastAPI(
    title="Raspberry Pi System Monitor",
    description="Simple API that exposes Raspberry Pi system metrics.",
    version="0.1.0",
)

## Allow frontend running on another origin (or same PI)
## Allow CORS support for our FastAPI application

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  ## any domain is allowed to make request on API
    allow_credentials=True,
    allow_methods=["*"],  ## allow HTTP methods
    allow_headers=["*"],  ## allow custom headers
)

## Define paths for frontend files
BASE_DIR = Path(__file__).resolve().parent       ## /backend/
FRONTEND_DIR = BASE_DIR.parent / "frontend"      ## /frontend/

## Mount static directory for frontend JavaScript + any assets
## This makes /static/script.js point to /frontend/script.js
app.mount(
    "/static",
    StaticFiles(directory=str(FRONTEND_DIR)),
    name="static"
)

## Serve the dashboard HTML file at the root URL "/"
@app.get("/")
def serve_dashboard():
    ## Return index.html directly
    return FileResponse(FRONTEND_DIR / "index.html")

## API endpoint: return the current system metrics snapshot
@app.get("/api/metrics/latest")
def read_latest_metrics():
    return get_system_metrics()

## API health endpoint
@app.get("/api/health")
def health_check():
    return {"status": "ok"}
