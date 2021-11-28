from typing import (
	Any,
	List,
	Optional,
)

from fastapi import (
	APIRouter,
	Depends,
	Request,
	HTTPException,
)


from app import schemas


from app.api import deps


from app.config.settings import settings


from app.extensions import limiter


from pymongo import MongoClient


import datetime


from app.utils.celo import kit, gold_token




router = APIRouter()




@router.get(
	'/balance',
)
async def balance(
	request: Request,
	*,
	db: MongoClient = Depends(deps.get_db),
	user: Any = Depends(deps.get_current_active_user),
) -> Any:
	# --

	try:
		user['celo_address']
	except ValueError:
		raise HTTPException(
			status_code=500,
			detail='No address',
		)


	balance = gold_token.balance_of(user['celo_address'])

	balance = kit.w3.fromWei(balance, 'ether')

	return {
		'balance': balance,
	}







