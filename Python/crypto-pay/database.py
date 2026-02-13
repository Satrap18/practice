import sqlite3
from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
import os
import hashlib


def create_wallet():
    client = Tron(HTTPProvider('https://api.nileex.io'))
    private_key = PrivateKey(os.urandom(32))
    wallet_address = private_key.public_key.to_base58check_address()
    return private_key.hex(), wallet_address

class DataBase:

    def __init__(self):
        super().__init__()

        self.con = sqlite3.connect('wallet.db')
        self.cur = self.con.cursor()

    
    def create_table(self):

        self.cur.execute('CREATE TABLE IF NOT EXISTS user (fullname TEXT, username TEXT, password TEXT, wallet TEXT)')

        # print('database create!')

    def create_user(self, fullname, username, password):

        private_key, wallet_address = create_wallet()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        data = (fullname, username, hashed_password, wallet_address)

        self.cur.execute('INSERT INTO user (fullname, username, password, wallet) VALUES (?,?,?,?)', data)
        self.con.commit()

        # print(f'User "{username}" created! Wallet: {wallet_address}')
        # print(f'Private Key (hex): {private_key}')

    def login_user(self, username, password):

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        res = self.cur.execute(f"SELECT username FROM user WHERE username=? AND password=?", (username, hashed_password))

        row = res.fetchone()

        if row:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password")

    def wallet_user(self, username):

        res = self.cur.execute(f"SELECT wallet FROM user WHERE username=?", (username,))

        row = res.fetchone()

        if row:
            return row[0]
        else:
            return None

    def cheak_user(self, username):

        data = self.cur.execute("SELECT username FROM user WHERE username=?", (username,))

        cheak = data.fetchone()

        if cheak:
            return cheak[0]
        else:
            return None
        

if __name__ == "__main__":
    main = DataBase()