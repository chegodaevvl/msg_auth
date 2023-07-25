from fastapi import APIRouter

from app.auth.auth_route import router as auth_routers

router = APIRouter()

router.include_router(auth_routers, prefix="/login", tags=["login"])
