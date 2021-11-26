from typing import (
	Any,
	List,
	Optional,
)

from fastapi import (
	APIRouter,
	Depends,
	Request,
)

from app.api import deps


from app.config.settings import settings


from app.extensions import limiter


from pymongo import MongoClient



router = APIRouter()



# from app.config.settings import settings

# from celo_sdk.kit import Kit


# kit = Kit('https://alfajores-forno.celo-testnet.org')



# escrow_contract = kit.base_wrapper.create_and_get_contract_by_name('Escrow')




@router.get(
	'/check-token/{token}',
)
def check_token(
	request: Request,
	*,
	token: str,
) -> Any:
	# --

	return {
		'msg': '...',
	}



@router.get(
	'/collect/{token}',
)
def collect_red_pocket_payment(
	request: Request,
	*,
	token: str,
) -> Any:
	# --

	# withdraw!

	pass







