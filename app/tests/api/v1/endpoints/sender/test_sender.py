import pytest


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from httpx import AsyncClient



from app.config.settings import settings


from app.tests.utils import (
	random_email,
	random_name,
	random_lower_string,
)


from typing import (
	Dict,
)


from pydantic import (
	EmailStr,
)



@pytest.mark.asyncio
async def test_create_pocket(
	client: AsyncClient,
	token_headers_user: Dict[str, str],
	db: MongoClient,
) -> None:
	# --

	# get user_id somehow...
	user = db['main']['users'].find_one()

	data = {
		'user_id': int(user['_id']),
		'celo_value_amount': 5.0,
		'recipients_amount': 4,
		'initial_txt': None,
		'txns': [],
	}

	resp = await client.post(
		f'{settings.API_V1_STR}/_sender/pockets',
		headers=token_headers_user,
		json=data,
	)

	assert resp.status_code == 200
	result = resp.json()






