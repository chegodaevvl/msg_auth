from fastapi import APIRouter, Depends
from app.auth.auth_bearer import JWTBearer

from app.routes.users import router as users_routers
from app.routes.messages import router as msg_routers

router = APIRouter()

router.include_router(users_routers, prefix="/users", dependencies=[Depends(JWTBearer())], tags=["users"])
router.include_router(msg_routers, prefix="/msgs", dependencies=[Depends(JWTBearer())], tags=["msgs"])
