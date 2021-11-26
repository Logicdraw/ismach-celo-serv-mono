from typing import (
	Generator,
	Any,
)

from fastapi import (
	Depends,
	HTTPException,
	status,
)

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from pydantic import ValidationError


from pymongo import MongoClient


from app.config.settings import settings



token_bearer = OAuth2PasswordBearer(
	tokenUrl='/_auth/login/access-token',
)



def get_db() -> Generator:
	# --
	try:
		yield mongo_client
	finally:
		mongo_client.close()



def get_current_user(
	db: MongoClient = Depends(get_db),
	*,
	token: str,
) -> Any:
	# --
	try:
		payload = jwt.decode(
			token,
			settings.SECRET_KEY.get_secret_value(),
			algorithms=[ALGORITHM],
		)
		token_data = TokenSchemaPayload(**payload)
	except (jwt.JWTError, ValidationError):
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail='Could not validate credentials!',
		)

	user = db['main']['users'].find_one(
		{
			'_id': token_data.sub,
		},
	)

	if not user:
		raise HTTPException(
			status_code=404,
			detail='User not found!',
		)

	return user



def get_current_active_user(
	current_user = Depends(get_current_user),
) -> Any:
	# Current active user --

	if not bool(current_user['is_active']):
		raise HTTPException(
			status_code=400,
			detail='Inactive user!',
		)

	return current_user



