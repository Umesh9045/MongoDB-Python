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

---

## **4. MongoDB Core Fundamentals (Short Revision)**

### **1. Basics**
#### Syntax:
```sh
show dbs  # List all databases
use mydatabase  # Switch to a database
show collections  # List collections
```
#### Example:
```sh
use library  # Switch to library database
```

### **2. CRUD Operations**
#### Syntax & Example:
```sh
# Create
collection.insert_one({"name": "John", "age": 30})

# Read
collection.find_one({"name": "John"})

# Update
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Delete
collection.delete_one({"name": "John"})
```

### **3. Data Types**
#### Supported Data Types:
- String, Number (int, double), Boolean, Array, Object, Date

#### Example:
```sh
{ "name": "Alice", "age": 25, "isMember": true, "skills": ["Python", "MongoDB"] }
```

### **4. Operators**
#### Example:
```sh
collection.find({ "age": { "$gt": 25 } })  # Greater than 25
```

### **5. Cursor Methods**
#### Example:
```sh
cursor = collection.find()
for doc in cursor:
    print(doc)
```

### **6. Aggregate Framework**
#### Example:
```sh
collection.aggregate([{ "$group": { "_id": "$city", "total": { "$sum": 1 } } }])
```

### **7. Aggregate with String Operator**
```sh
collection.aggregate([{ "$project": { "fullName": { "$concat": ["$firstName", " ", "$lastName"] } } }])
```

### **8. Aggregate with Arithmetic Operator**
```sh
collection.aggregate([{ "$project": { "doubleAge": { "$multiply": ["$age", 2] } } }])
```

### **9. Conditions (if-else)**
```sh
collection.aggregate([{ "$project": { "ageGroup": { "$cond": { "if": { "$gte": ["$age", 18] }, "then": "Adult", "else": "Minor" } } } }])
```

### **10. Variables**
```sh
let ageLimit = 30;
collection.find({ "age": { "$gte": ageLimit } })
```

### **11. Data Modeling**
```sh
{
    "_id": ObjectId("..."),
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
```

### **12. Schema Validation**
```sh
db.createCollection("users", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "age"],
         properties: {
            name: {
               bsonType: "string",
               description: "must be a string"
            },
            age: {
               bsonType: "int",
               minimum: 18,
               description: "must be an integer >= 18"
            }
         }
      }
   }
})
```

### **13. Transactions**
```sh
session = client.start_session()
session.start_transaction()
try:
    collection.insert_one({"name": "Alice"}, session=session)
    collection.insert_one({"name": "Bob"}, session=session)
    session.commit_transaction()
except:
    session.abort_transaction()
```

### **14. Replica**
```sh
rs.initiate()
rs.status()
```


## **5. Create (Insert Data)**
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

## **6. Read (Retrieve Data)**
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

## **7. Update (Modify Data)**
```python
# Update one document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# Update multiple documents
collection.update_many({"city": "Los Angeles"}, {"$set": {"city": "San Francisco"}})
```

## **8. Delete (Remove Data)**
```python
# Delete one document
collection.delete_one({"name": "Alice"})

# Delete multiple documents
collection.delete_many({"age": {"$lt": 25}})  # Remove users younger than 25
```
