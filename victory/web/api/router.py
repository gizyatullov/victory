from fastapi.routing import APIRouter

from victory.web.api import assortment, auth, division, docs, echo, monitoring, user

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(assortment.router, prefix="/assortment", tags=["assortment"])
api_router.include_router(division.router, prefix="/division", tags=["division"])
