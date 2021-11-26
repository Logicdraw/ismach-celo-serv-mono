from typing import (
	Any,
	Dict,
	List,
	Optional,
	Union,
)


from pydantic import (
	AnyHttpUrl,
	BaseSettings,
	EmailStr,
	HttpUrl,
	PostgresDsn,
	validator,
	SecretStr,
)


import os



from dotenv import load_dotenv
load_dotenv()




if 'VERCEL' in os.environ:
	in_prod = (os.environ['VERCEL_ENV'] == 'production')
	in_staging = (os.environ['VERCEL_ENV'] == 'preview')
	in_server = True
else:
	in_prod = in_staging = in_server = False


in_testing = ('TESTING' in os.environ)


in_local = not in_server

in_dev = in_local and not in_testing




base_dir = os.path.abspath(
			os.path.dirname(
				os.path.dirname(
					os.path.dirname(__file__) )))





class Settings(BaseSettings):

	PROJECT_NAME: str = 'ismach-celo-serv-mono'


	DEVELOPMENT: bool = in_dev

	TESTING: bool = in_testing

	STAGING: bool = in_staging

	PRODUCTION: bool = in_prod


	API_V1_STR: str = '/api/v1'



	BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
		# Local/Development
		'http://localhost:3000',
		'http://localhost:5000',
		# --
	]


	@validator(
		'BACKEND_CORS_ORIGINS',
		pre=True,
	)
	def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
		if isinstance(v, str) and not v.startswith("["):
			return [i.strip() for i in v.split(",")]
		elif isinstance(v, (list, str)):
			return v
		raise ValueError(v)


	MONGO_DEV_DB: str
	MONGO_DEV_HOST: str
	MONGO_DEV_USER: str
	MONGO_DEV_PASSWORD: SecretStr

	MONGO_DEV_URI: Optional[str] = None

	@validator(
		'MONGO_DEV_URI',
		pre=True,
	)
	def assemble_mongo_dev_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('MONGO_DEV_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}?retryWrites=true&w=majority'.format(
			scheme='mongodb+srv',
			user=values.get('MONGO_DEV_USER'),
			password=password.get_secret_value(),
			host=values.get('MONGO_DEV_HOST'),
			db=values.get('MONGO_DEV_DB'),
		)

	MONGO_DEV_MIN_CONNECTIONS_COUNT: Optional[int] = os.environ['MONGO_DEV_MIN_CONNECTIONS_COUNT']
	MONGO_DEV_MAX_CONNECTIONS_COUNT: Optional[int] = os.environ['MONGO_DEV_MAX_CONNECTIONS_COUNT']




	SECRET_KEY: SecretStr = os.environ['SECRET_KEY']


	CELO_ADDRESS_1: str = os.environ['CELO_ADDRESS_1']
	CELO_ADDRESS_PRIVATE_KEY_1: SecretStr = os.environ['CELO_ADDRESS_PRIVATE_KEY_1']

	CELO_ADDRESS_2: str = os.environ['CELO_ADDRESS_2']
	CELO_ADDRESS_PRIVATE_KEY_2: SecretStr = os.environ['CELO_ADDRESS_PRIVATE_KEY_2']


	CELO_ADDRESS_3: str = os.environ['CELO_ADDRESS_3']

	CELO_ADDRESS_4: str = os.environ['CELO_ADDRESS_4']

	CELO_ADDRESS_5: str = os.environ['CELO_ADDRESS_5']
	
	CELO_ADDRESS_6: str = os.environ['CELO_ADDRESS_6']



	# CELO_RED_POCKET_LINK: str = os.environ['CELO_RED_POCKET_LINK']


	USER_1_USERNAME: str = os.environ['USER_1_USERNAME']
	USER_1_EMAIL: str = os.environ['USER_1_EMAIL']
	USER_1_PASSWORD: SecretStr = os.environ['USER_1_PASSWORD']

	USER_2_USERNAME: str = os.environ['USER_2_USERNAME']
	USER_2_EMAIL: str = os.environ['USER_2_EMAIL']
	USER_2_PASSWORD: SecretStr = os.environ['USER_2_PASSWORD']

	USER_3_USERNAME: str = os.environ['USER_3_USERNAME']
	USER_3_EMAIL: str = os.environ['USER_3_EMAIL']
	USER_3_PASSWORD: SecretStr = os.environ['USER_3_PASSWORD']

	USER_4_USERNAME: str = os.environ['USER_4_USERNAME']
	USER_4_EMAIL: str = os.environ['USER_4_EMAIL']
	USER_4_PASSWORD: SecretStr = os.environ['USER_4_PASSWORD']

	USER_5_USERNAME: str = os.environ['USER_5_USERNAME']
	USER_5_EMAIL: str = os.environ['USER_5_EMAIL']
	USER_5_PASSWORD: SecretStr = os.environ['USER_5_PASSWORD']

	USER_6_USERNAME: str = os.environ['USER_6_USERNAME']
	USER_6_EMAIL: str = os.environ['USER_6_EMAIL']
	USER_6_PASSWORD: SecretStr = os.environ['USER_6_PASSWORD']


	if in_local:
		pass


	if in_dev:

		SERVER_NAME: str = '127.0.0.1:8000'

		SERVER_HOST: Optional[str] = None

		@validator(
			'SERVER_HOST',
			pre=True,
		)
		def assemble_server_host(
			cls,
			v: Optional[str],
			values: Dict[str, Any],
		) -> Any:
			if isinstance(v, str):
				return v
			return 'http://{}'.format(values.get('SERVER_NAME'))


		CLI_PASSWORD: str = os.environ['CLI_PASSWORD']



	if in_testing:
		pass		


	if in_server:
		pass


	if in_staging:
		pass
		

	if in_prod:
		pass



	class Config:
		case_sensitive = True

		# env_file = '.env'




settings = Settings()






