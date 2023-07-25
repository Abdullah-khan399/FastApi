from fastapi import APIRouter
from MyFastApi.app.api.v1 import resource


api_router = APIRouter()
api_router.include_router(resource.router)
