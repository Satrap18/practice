import sqlite3

class DataBase:

    def __init__(self):
        super().__init__()

        self.con = sqlite3.connect('wallet.db')
        self.cur = self.con.cursor()

    
    def create_table(self):

        self.cur.execute('CREATE TABLE IF NOT EXISTS user (fullname TEXT, username TEXT, password TEXT, wallet TEXT)')
        print('database create!')

    def create_user(self, fullname, username, password, wallet):

        data = (fullname, username, password, wallet)

        self.cur.execute('INSERT INTO user (fullname, username, password, wallet) VALUES (?,?,?,?)', data)
        self.con.commit()
        self.con.close()

        print('User Create')

    def login_user(self, username, password):

        res = self.cur.execute(f"SELECT username FROM user WHERE username=? AND password=?", (username, password))

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

if __name__ == "__main__":
    main = DataBase()
