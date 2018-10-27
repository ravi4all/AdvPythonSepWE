import re

text = "Hello Ram, How are you ?"

data = re.search('[a-z]\w+', text)
print(data)

# data = re.findall('[A-Z]\w+', text)
# print(data)