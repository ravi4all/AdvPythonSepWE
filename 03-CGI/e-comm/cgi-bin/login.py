import cgi
import pymysql
import header
import content

form = cgi.FieldStorage()

email = form.getvalue('email')
pwd = form.getvalue('pwd')

# email = 'ram@gmail.com'
# pwd = '1234'

connection = pymysql.connect(host = 'localhost',
                port = 3306,
                user = 'root',
                db = 'e_comm2',
                autocommit = True)

cursor = connection.cursor()

query = "SELECT * FROM users WHERE email = %s AND pwd = %s"
cursor.execute(query, (email,pwd))

data = cursor.fetchall()
print(data)
if len(data) < 1:
    msg = "User do not exist"
    print(msg)
else:
    print("Login Success")
    reg = True
    header.head(reg, data[0][0])

# print(data)
content.products()