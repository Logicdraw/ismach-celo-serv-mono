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


from app import schemas


from app.api import deps


from app.config.settings import settings


from app.extensions import limiter


from pymongo import MongoClient


import datetime



router = APIRouter()



from app.utils.celo import kit




@router.get(
	'/collect/{slug}',
)
async def collect_pocket_payment(
	request: Request,
	*,
	db: MongoClient = Depends(deps.get_db),
	user: Any = Depends(deps.get_current_active_user),
	slug: str,
) -> Any:
	# --

	pocket = db['main']['pockets'].find_one(
		{'generated_slug': slug}
	)

	if not pocket:
		raise HTTPException(
			status_code=404,
			detail='Coach not found!',
		)

	if str(user['_id']) in pocket['txns'].keys():
		if bool(pocket['txns'][user['_id']]):
			raise HTTPException(
				status_code=500,
				detail='Collected payment already!',
			)


	if len(pocket['txns']) >= pocket['recipients_amount']:
		raise HTTPException(
			status_code=500,
			detail='Not in time!',
		)



	pocket['txns'][str(user['_id'])] = ''
	new_pocket_txns = pocket['txns']

	db['main']['pockets'].update_one(
		{'generated_slug': slug},
		{new_pocket_txns}
	)


	celo_value_amount = pocket['celo_value_amount'] * 0.5

	try:
		kit.wallet_change_account = settings.CELO_ADDRESS_2
		celo_amount = kit.w3.toWei(celo_value_amount, 'ether')
		tx_hash = gold_token.transfer(settings.CELO_ADDRESS_2, celo_amount)
	except:
		raise HTTPException(
			status_code=500,
			detail='Error sending payment',
		)

	
	pocket['txns'][str(user['_id'])] = tx_hash
	new_pocket_txns = pocket['txns']


	db['main']['pockets'].update_one(
		{'generated_slug': slug},
		{new_pocket_txns}
	)


	return {
		'msg': f'You have received {celo_value_amount} CELO! Txn: {tx_hash}',
	}







