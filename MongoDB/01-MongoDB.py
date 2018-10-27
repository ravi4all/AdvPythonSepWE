# pip install pymongo
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.testDB

p_id = 102
p_name = "Samsung"
p_price = 50000

def insert_data():
    db.products.insert({"p_id":p_id,
                        "p_name":p_name,
                        "p_price":p_price
                        })
    print("Data Inserted Successfully...")

def select_data():
    data = db.products.find()
    for row in data:
        print(row)

def where_clause():
    data = db.products.find({"p_name":"Apple"})
    for row in data:
        print(row)

# insert_data()
# select_data()
where_clause()