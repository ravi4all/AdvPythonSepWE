import re

pattern = '[a-z | 0-9]\w+[@]+[a-z]\w+[.]+[a-z]\w{2,}'

emails = ['ram@gmail.com',
          'ram_1234@gmail.com',
          'ram12shyam@gmail.com',
          'ram$12shyam@gmail',
          'ram12@gmail.com.in',
          'Ram123@gmail,com',
          'shyam-123@gmail.com'
          ]

for i in range(len(emails)):
    if re.search(pattern, emails[i]):
        print("Welcome",emails[i])