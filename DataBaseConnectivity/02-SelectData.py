import pymysql

connection = pymysql.connect(host = 'localhost',
                            port = 3306,
                            user = 'root',
                            db = 'testEngine_2',
                            autocommit = True)

cursor = connection.cursor()

t_id = 101
t_pwd = 22323

query = "SELECT * FROM teachers WHERE t_id = %s and t_pwd = %s"
cursor.execute(query, (t_id, t_pwd))

# print(cursor)
for data in cursor:
    print(data)