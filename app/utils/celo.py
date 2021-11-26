from app.config.settings import settings

from celo_sdk.kit import Kit


kit = Kit('https://alfajores-forno.celo-testnet.org')



escrow_contract = kit.base_wrapper.create_and_get_contract_by_name('Escrow')


escrow_contract.transfer(
	from_addr=settings.CELO_ADDRESS_1,
	identifier=None,
	token=None,
	value=None,
	payment_id=None,
)


# transfer ...


# # what would be the util functions????

# kit.w3.eth.getBalance(some_address)







