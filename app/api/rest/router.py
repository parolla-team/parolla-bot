from fastapi import APIRouter

from app.api.rest.routes.v1 import health
from app.api.rest.routes.v1 import user_api as user_v1

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(health.router, tags=["health"])
router.include_router(user_v1.router, tags=["user"])
