from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
import os

client = Tron(HTTPProvider('https://api.nileex.io'))

private_key = PrivateKey(os.urandom(32))

print('Private Key (hex):', private_key.hex())
print('Address (base58):', private_key.public_key.to_base58check_address())
