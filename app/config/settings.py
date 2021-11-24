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



	SECRET_KEY: SecretStr = os.environ['SECRET_KEY']


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






