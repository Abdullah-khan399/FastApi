from fastapi import APIRouter
from MyFastApi.app.api.v1.model import Home

router = APIRouter()


@router.post("/")
def home(model: Home):
    return {"name": model.name}
