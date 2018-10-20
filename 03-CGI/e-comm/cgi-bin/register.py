import cgi
import pymysql
import header
import content

form = cgi.FieldStorage()

name = form.getvalue('u_name')
email = form.getvalue('u_email')
pwd = form.getvalue('u_pwd')
mobile = form.getvalue('u_num')
city = form.getvalue('u_city')

connection = pymysql.connect(host = 'localhost',
                port = 3306,
                user = 'root',
                db = 'e_comm2',
                autocommit = True)

cursor = connection.cursor()

query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s)"
cursor.execute(query, (name,email,pwd,mobile,city))

reg = True
header.head(reg, name)
content.products()