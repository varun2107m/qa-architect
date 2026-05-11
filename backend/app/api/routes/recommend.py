from fastapi import APIRouter

from backend.app.engine.recommendation_engine import (
    recommend_framework
)

router = APIRouter()


@router.get("/recommend")
def recommend():

    result = recommend_framework([
        "parallel_execution",
        "api_testing"
    ])

    return result