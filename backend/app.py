## /backend/api
## this will use fastAPI to use build an API communicate with the front end

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metrics import get_system_metrics ## from /backend/metrics.py

## Build the app

app = FastAPI(
    title = "Raspberry Pi System Monitor",
    description = "Simple API that exposes Raspberry Pi system metrics.",
    version = "0.1.0",
)

## Allow frontend runnig on another origin(or same PI)
## Allow CORS support for our FastAPI application

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"], ## any domain is allowed to make request on API
    allow_credentials = True,
    allow_methods = ["*"], ## allow HTTP methods
    allow_headers = ["*"], ## allow custom headers
)

@app.get("/api/metrics/latest")
def read_latest_metrics():
    # Return the cyrrent system metrics snapshot
    return get_system_metrics()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
