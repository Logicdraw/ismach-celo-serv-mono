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

from app.api import deps


from app import schemas


from app.config.settings import settings


from app.extensions import limiter


from bson import ObjectId



router = APIRouter()



# from app.config.settings import settings

# from celo_sdk.kit import Kit


# kit = Kit('https://alfajores-forno.celo-testnet.org')



# escrow_contract = kit.base_wrapper.create_and_get_contract_by_name('Escrow')




@router.post(
	'/pockets-test',
)
def create_pocket_test(
	request: Request,
	*,
	db: MongoClient = Depends(deps.get_db),
	user: Any = Depends(deps.get_current_active_user),
	pocket_in: schemas.PocketSchemaCreate,
) -> Any:
	# --

	try:
		# web3 my contract
		pass
	except:
		raise HTTPException(
			status=500,
			detail='Not working!',
		)

	db['main']['pockets'].insert_one(pocket_in.to_dict())

	# need to generate link!

	return {
		'msg': 'Text!',
	}






# @router.post(
# 	'/red-pockets',
# )
# def create_red_pocket(
# 	request: Request,
# 	# *,
# 	# ---
# ) -> Any:
# 	# --

# 	escrow_contract.transfer()


# 	return {
# 		'msg': 'Text!',
# 	}




# route:

# -- create a payment!


# -- receive a payment (no address just yet!)






# what sort of payments.




# ---
# ...




# @router.post(
# 	'/',
# )
# @limiter.limit('120/minute')




# @router.get(
# 	'/link/{link}',
# )
# def read_link(
# 	request: Request,
# 	*,
# 	link: str,
# ) -> Any:
# 	# --
# 	pass







