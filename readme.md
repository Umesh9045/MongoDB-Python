# MongoDB CRUD Cheat Sheet (Python)

## **1. What is MongoDB?**
MongoDB is a NoSQL database that stores data in JSON-like documents instead of tables. Unlike SQL databases, MongoDB is schema-less, meaning you don't have to define a fixed structure before inserting data. It is highly scalable and designed for handling large amounts of unstructured data.

### **How MongoDB Differs from SQL?**
| Feature      | MongoDB (NoSQL)       | SQL Databases         |
|-------------|----------------------|----------------------|
| Data Storage | JSON-like documents  | Tables & Rows       |
| Schema      | Schema-less          | Predefined Schema   |
| Scalability | Horizontally scalable | Vertically scalable |
| Joins       | Not required (Embedded documents) | Requires joins |
| Flexibility | More flexible         | Rigid structure     |

---

## **2. Installation and Setup**

### **Install MongoDB**
- Download and install MongoDB from [MongoDB Official Site](https://www.mongodb.com/try/download/community)
- Start MongoDB server:
  ```sh
  mongod
  ```

### **Install pymongo (Python MongoDB Driver)**
```sh
pip install pymongo
```

---

## **3. Connect to MongoDB**
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
db = client["mydatabase"]  # Select or create database
collection = db["users"]  # Select or create collection
```

## **4. Create (Insert Data)**
```python
# Insert one document
user = {"name": "Alice", "age": 25, "city": "New York"}
collection.insert_one(user)

# Insert multiple documents
users = [
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 22, "city": "Chicago"},
]
collection.insert_many(users)
```

## **5. Read (Retrieve Data)**
```python
# Fetch one document
user = collection.find_one({"name": "Alice"})
print(user)

# Fetch all documents
for user in collection.find():
    print(user)

# Fetch with a condition
for user in collection.find({"age": {"$gt": 25}}):  # Age greater than 25
    print(user)
```

## **6. Update (Modify Data)**
```python
# Update one document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# Update multiple documents
collection.update_many({"city": "Los Angeles"}, {"$set": {"city": "San Francisco"}})
```

## **7. Delete (Remove Data)**
```python
# Delete one document
collection.delete_one({"name": "Alice"})

# Delete multiple documents
collection.delete_many({"age": {"$lt": 25}})  # Remove users younger than 25
```
