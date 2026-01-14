import pymysql

class DataBase:

    def __init__(self):
        
        self.host = 'localhost'
        self.password = 'MyRootPass@2024'
        self.user = 'root'
        self.port = 3306

    def connect(self):

        try:
            con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
            print('DataBase Connect!')
        except:
            print("Can't Connect To Database Check Your Data!")

    def create_database(self, databasename):

        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {databasename}")
        con.commit()
        con.close()
        print('DataBase Create!')

    def create_table(self,databasename ,table_name, value):

        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f'USE {databasename}')
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({value})")
        con.commit()
        con.close()
        print('Create Table on DataBase')

    def insert_data_table(self, databasename, tablename, fields:str, vlaue):
        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f'USE {databasename}')
        cur.execute(f"INSERT INTO {tablename}({fields}) VALUES ('{vlaue}')")
        con.commit()
        con.close()
        print(f'Insert Data on {databasename} DataBase')

    def delete_data_table(self, databasename, tablename, fields, value):

        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f'USE {databasename}')
        cur.execute(f"DELETE FROM {tablename} WHERE {fields} = '{value}'")
        con.commit()
        con.close()
        print(f'Delete Speic Data In {tablename}')

    def delete_table_database(self, databasename, tablename):

        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f'USE {databasename}')
        cur.execute(f"DROP TABLES {tablename}")
        con.commit()
        con.close()
        print(f'Delete Table {tablename}')

    def delete_database(self, databasename):

        con = pymysql.connect(host=self.host, user=self.user, passwd=self.password, port=self.port)
        cur = con.cursor()
        cur.execute(f"DROP DATABASE {databasename}")
        con.commit()
        con.close()
        print(f'Delete DataBase {databasename}')

database = DataBase()

database.host = "127.0.0.1"
database.password = 'MyRootPass@2024'
database.user = 'root'
database.port = 3306

# database.connect()
# database.create_database('practices')
# database.create_table('practices','fullname', 'name varchar(30)')
# database.insert_data_table('practices','fullname', 'name', 'Mohammadrezadasda')
# database.insert_data_table('practices','fullname', 'name', 'Satrap18ds')
# database.delete_data_table('practices', 'fullname', 'name', 'MohammadReza2')
# database.delete_table_database('practices', 'fullname')
# database.delete_database('practices')