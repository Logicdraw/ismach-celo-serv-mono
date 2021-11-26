from fastapi import APIRouter


from app.api.v1.endpoints import (
	auth,
	receiver,
	sender,
)

from app.config.settings import settings



api_v1_router = APIRouter(
	prefix=settings.API_V1_STR,
)


api_v1_router.include_router(
	auth.router,
	prefix='/_auth',
	tags=['receiver'],
)

api_v1_router.include_router(
	receiver.router,
	prefix='/_receiver',
	tags=['receiver'],
)

api_v1_router.include_router(
	sender.router,
	prefix='/_sender',
	tags=['sender'],
)


