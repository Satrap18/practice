from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
import os

# Connect to testnet #
client = Tron(HTTPProvider('https://api.nileex.io'))

# create random 32 number for new wallet #
# private_key = PrivateKey(os.urandom(32))

# use private key (hex) #
private_key = PrivateKey(bytes.fromhex("5e5fa8733b84fa1c6d85908af3c84a78a9a745d118ede31424ff37ea9ad4a200"))

# show wallet adress and private key #
print('Private Key (hex):', private_key.hex())

# The payment address depends only on the value of the private key #
print('Address (base58):', private_key.public_key.to_base58check_address())

# Using a fixed wallet without changing it #
address = private_key.public_key.to_base58check_address()

# show (SUN) balance account #
balance_sun = client.get_account_balance(address)
print("Balance (SUN):", balance_sun)

# show (TRX) balance account #
balance_trx = balance_sun / 1_000_000
print("Balance (TRX):", balance_trx)

# send balance to another wallet #
from_address = private_key.public_key.to_base58check_address()

# create a new wallet address for send balance #
dest_private_key = PrivateKey(os.urandom(32))
to_address = dest_private_key.public_key.to_base58check_address()

print("sending to:", to_address)

amount = int(0.001 * 1_000_000)

txn = (client.trx.transfer(from_address, to_address, amount).build().sign(private_key))

result = txn.broadcast()

print("Broadcast Result:", result)
print("Transaction ID:", txn.txid)

# confirmed = txn.wait()
# print("Transaction Confirmed:", confirmed)


balance_sun = client.get_account_balance(to_address)
balance_trx = balance_sun / 1_000_000
print("Destination Balance (TRX):", balance_trx)