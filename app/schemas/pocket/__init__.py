from typing import (
	Optional,
	Any,
)

from pydantic import (
	BaseModel,
	EmailStr,
	validator,
	Field,
)




class PocketSchemaBase(BaseModel):
	user_id: Optional[str] = None
	celo_value_amount: Optional[float] = None
	recipients_amount: Optional[int] = None
	txns: Optional[dict] = None



class PocketSchemaCreate(
	PocketSchemaBase,
):
	user_id: str


class PocketSchemaUpdate(
	PocketSchemaBase,
):
	pass


class PocketSchemaInDBBase(
	PocketSchemaBase,
):
	id: str

	class Config:
		fields = {'id': '_id'}



class PocketSchema(
	PocketSchemaInDBBase,
):
	pass
	



class PocketSchemaInDB(
	PocketSchemaInDBBase,
):
	pass




