from fastapi import APIRouter
from ml_models import RecommendationModel

router = APIRouter()

try:
    recommend = RecommendationModel()
    recommend.train()
    # recommend.save()
except Exception as e:
    print(f"Model training failed: {e}")
    recommend = None


@router.get("/product/{id}/recommendation")
def get_recommendation(product_id: int):

    # recommend.load()
    return recommend.recommend(product_id)
