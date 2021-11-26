# --

from typing import (
	List,
	Optional,
	Any,
)

from bson import ObjectId


import datetime


from app.security import (
	get_password_hash,
	verify_password,
)


from app.schemas.user import (
	UserSchema,
	UserSchemaCreate,
	UserSchemaUpdate,
)


from pymongo import MongoClient


from app.database.client import (
	MONGO_DB,
)



class UsersCRUD:
	# --

	collections_name: str = 'users'


	def get_by_email(
		self,
		db: MongoClient,
		*,
		email: str,
	) -> Optional[Any]:
		# --

		user = db[MONGO_DB][UsersCRUD.collections_name].find_one({
			{ "email": {"$regex": email.lower(), "$options":"i"} }
		})

		return user


	def authenticate(
		self,
		db: MongoClient,
		*,
		email: str,
		password: str,
	) -> Any:
		# --

		user = self.get_by_email(
			db=db,
			email=email,
		)

		if not user:
			return None

		if not verify_password(password, user['password_hash']):
			return None

		return user


	def create(
		self,
		db: MongoClient,
		obj_in: UserSchemaCreate,
	) -> Any:
		# --

		user_in = obj_in.dict(
			exclude={
				'password',
				'confirm_password',
			}
		)

		user_in['password_hash'] = get_password_hash(obj_in.password)

		inserted_user = db[MONGO_DB]['users'].insert_one(user_in)

		user_in['id'] = inserted_user.inserted_id

		return user_in




users_crud = UsersCRUD()

