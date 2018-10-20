#!C:/Python36/python.exe
import cgi

form = cgi.FieldStorage()

email = form.getvalue('email')
pwd = form.getvalue('pwd')

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")

if email == 'ram@gmail.com' and pwd == '1234':
    print("<h1>Hello {}</h1>".format(email))
else:
    print("<h1>Invalid User</h1>")

print("""
</body>
</html>
""")