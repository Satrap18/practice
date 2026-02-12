from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey

client = Tron(HTTPProvider("https://api.nileex.io"))

private_key_hex = "5e5fa8733b84fa1c6d85908af3c84a78a9a745d118ede31424ff37ea9ad4a200"
private_key = PrivateKey(bytes.fromhex(private_key_hex))

wallet_address = private_key.public_key.to_base58check_address()
print("Wallet Address:", wallet_address)

USDT_CONTRACT_ADDRESS = "TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj"

contract = client.get_contract(USDT_CONTRACT_ADDRESS)

balance_smallest_unit = contract.functions.balanceOf(wallet_address)

balance_usdt = balance_smallest_unit / 1_000_000

print("USDT Balance:", balance_usdt)