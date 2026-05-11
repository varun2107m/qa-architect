from fastapi import FastAPI

from backend.app.api.routes.generate import router as generate_router
from backend.app.api.routes.validate import router as validate_router
from backend.app.api.routes.recommend import router as recommend_router
from backend.app.api.routes.download import router as download_router


# -----------------------
# APP INITIALIZATION
# -----------------------
app = FastAPI(
    title="QA Architecture Agent",
    version="1.0.0",
    description="AI-powered QA Framework Generator"
)


# -----------------------
# ROUTE REGISTRATION
# -----------------------
app.include_router(generate_router)

app.include_router(validate_router)

app.include_router(recommend_router)

app.include_router(download_router)


# -----------------------
# HEALTH CHECK ENDPOINT
# -----------------------
@app.get("/")
def root():

    return {
        "status": "running",
        "service": "QA Architecture Agent",
        "mode": "AI_ARCHITECT_MODE"
    }
