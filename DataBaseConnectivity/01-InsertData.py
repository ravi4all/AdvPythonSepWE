# pip install pymysql
import pymysql

connection = pymysql.connect(host = 'localhost',
                            port = 3306,
                            user = 'root',
                            db = 'testEngine_2',
                            autocommit = True)

cursor = connection.cursor()

# query = "INSERT INTO teachers VALUES (101,'Gopal', 'IT', '22323')"

t_id = 101
t_name = 'Ram'
t_dept = 'ME'
t_pwd = '12232312'

query = "INSERT INTO teachers VALUES (%s, %s, %s, %s)"
cursor.execute(query, (t_id, t_name, t_dept, t_pwd))
print("Data Inserted Successfully...")