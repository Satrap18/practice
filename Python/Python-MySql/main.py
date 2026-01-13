import pymysql


try:
    con = pymysql.connect(host='localhost', user='root', passwd="MyRootPass@2024", port=3306)
    cur = con.cursor()
except:
    ValueError("Can't Connect To Database Check Your Data!")

# cur.execute("CREATE DATABASE IF NOT EXISTS practice")
# print('DataBase Create!')

cur.execute('USE practice')
print('Use practice DataBase')

# cur.execute("CREATE TABLE IF NOT EXISTS Fullname(name varchar(15), lastname varchar(15))")
# print('Create Table on practice DataBase')

# data = ('MohammadReza', 'Karimi')
# cur.execute("INSERT INTO Fullname(name, lastname) VALUES ('MohammadReza', 'Karimi')")
# print('Insert Data on Fullname DataBase')

# Delete Data In Tables #
# cur.execute("DELETE FROM Fullname WHERE name = 'NULL'")
# print('Delete Speic Data In Database')


# Delete Table in DataBase #
cur.execute("DROP TABLES Fullname")




con.commit()
con.close()