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


from pymongo import MongoClient



router = APIRouter()


import string

import random



from app.utils.celo import kit




def generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	# --

	return ''.join(random.choice(chars) for _ in range(size))




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
		kit.wallet_change_account = settings.CELO_ADDRESS_1
		celo_amount = kit.w3.toWei(pocket_in.celo_value_amount, 'ether')
		tx_hash = gold_token.transfer(settings.CELO_ADDRESS_1, celo_amount)
	except:
		raise HTTPException(
			status=500,
			detail='Not working!',
		)

	pocket_in.initial_txn = tx_hash

	slug = generator()
	pocket_in.generated_slug = slug

	db['main']['pockets'].insert_one(pocket_in.to_dict())


	return {
		'link': f'{slug}',
	}





