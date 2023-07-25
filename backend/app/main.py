from fastapi import Depends, FastAPI

from app.settings import settings
from app.routes import router as api_router
from app.auth import router as auth_router


def create_app() -> FastAPI:
    """
    Фабрика создания приложения FastAPI
    :return: приложение FastAPI
    """
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(
        api_router, prefix=settings.API_PREFIX
    )
    app.include_router(
        auth_router, prefix=settings.API_PREFIX
    )

    @app.get("/", tags=["root"])
    async def root() -> dict:
        return {
            "message": "Coolest service"
        }

    return app


app = create_app()
