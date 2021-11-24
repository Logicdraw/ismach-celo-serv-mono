from typing import (
	Generator,
)

from fastapi import (
	Depends,
	HTTPException,
	status,
)

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from pydantic import ValidationError



from app.config.settings import settings



token_bearer = OAuth2PasswordBearer(
	tokenUrl='',
)


def authenticate_request(
	token: str = Depends(token_bearer),
) -> None:
	# Authenticate request --

	if token != settings.SECRET_KEY.get_secret_value():
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail='Could not validate credentials!',
		)

	return None
		

