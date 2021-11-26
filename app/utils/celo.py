from app.config.settings import settings

from celo_sdk.kit import Kit


kit = Kit('https://alfajores-forno.celo-testnet.org')


kit.wallet_add_new_key = settings.CELO_ADDRESS_PRIVATE_KEY_1.get_secret_value()

kit.wallet_add_new_key = settings.CELO_ADDRESS_PRIVATE_KEY_2.get_secret_value()









