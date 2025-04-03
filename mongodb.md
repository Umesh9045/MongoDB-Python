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

## **3. MongoDB Core Fundamentals (Short Revision with Real-World Use Cases)**

### **1. Basics**
#### **Real-World Use Case**: Setting up a MongoDB database for an e-commerce platform.
#### **Syntax:**
```sh
show dbs  # List all databases
use ecommerce  # Switch to a database
show collections  # List collections
```
#### **Example:**
```sh
use ecommerce  # Switch to ecommerce database
```

### **2. CRUD Operations**
#### **Real-World Use Case**: Managing user accounts in a web application.
#### **Syntax & Example:**
```sh
# Create
collection.insert_one({"name": "John", "age": 30, "email": "john@example.com"})

# Read
collection.find_one({"email": "john@example.com"})

# Update
collection.update_one({"email": "john@example.com"}, {"$set": {"age": 31}})

# Delete
collection.delete_one({"email": "john@example.com"})
```

### **3. Data Types**
#### **Real-World Use Case**: Defining user attributes in a social media application.
#### **Types and Examples:**
| Data Type  | Description | Example |
|-----------|------------|---------|
| String    | Text data  | "Alice" |
| Number    | Integer, Double | 25, 3.14 |
| Boolean   | True/False | true |
| Array     | List of values | ["Python", "MongoDB"] |
| Object    | Embedded document | {"city": "NY", "zip": "10001"} |
| Date      | Timestamp | ISODate("2023-01-01T00:00:00Z") |

### **4. Operators**
#### **Real-World Use Case**: Filtering customers based on age.
#### **Operators Table:**
| Operator | Description | Example |
|----------|------------|---------|
| $gt      | Greater than | { "age": { "$gt": 25 } } |
| $lt      | Less than | { "age": { "$lt": 30 } } |
| $eq      | Equal to | { "status": { "$eq": "active" } } |
| $ne      | Not equal | { "status": { "$ne": "inactive" } } |
| $in      | Matches values in array | { "category": { "$in": ["A", "B"] } } |

### **5. Cursor Methods**
#### **Real-World Use Case**: Paginating products in an online store.
#### **Cursor Methods Table:**
| Method | Description |
|--------|------------|
| find() | Retrieve all documents |
| limit(n) | Limit the number of documents |
| sort() | Sort documents |
| count() | Count the number of documents |
| skip(n) | Skip first `n` documents |

### **6. Aggregate Framework**
#### **Real-World Use Case**: Calculating total sales per city.
#### **Aggregation Stages Table:**
| Stage | Description |
|-------|------------|
| $match | Filters documents |
| $group | Groups documents |
| $sort  | Sorts documents |
| $project | Reshapes documents |
| $limit  | Limits results |

### **7. Aggregate with String Operator**
#### **Real-World Use Case**: Creating full names in a user database.
#### **Syntax & Example:**
```sh
collection.aggregate([{ "$project": { "fullName": { "$concat": ["$firstName", " ", "$lastName"] } } }])
```

### **8. Aggregate with Arithmetic Operator**
#### **Real-World Use Case**: Calculating double salary for bonus calculations.
#### **Syntax & Example:**
```sh
collection.aggregate([{ "$project": { "doubleSalary": { "$multiply": ["$salary", 2] } } }])
```

### **9. Conditions (if-else)**
#### **Real-World Use Case**: Categorizing users based on age.
#### **Syntax & Example:**
```sh
collection.aggregate([{ "$project": { "ageGroup": { "$cond": { "if": { "$gte": ["$age", 18] }, "then": "Adult", "else": "Minor" } } } }])
```

### **10. Variables**
#### **Real-World Use Case**: Querying users above a dynamic age limit.
#### **Syntax & Example:**
```sh
let ageLimit = 30;
collection.find({ "age": { "$gte": ageLimit } })
```

### **11. Data Modeling**
#### **Real-World Use Case**: Structuring user profile data in a job portal.
#### **Syntax & Example:**
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
#### **Real-World Use Case**: Ensuring data consistency for an employee database.

### **13. Transactions**
#### **Real-World Use Case**: Ensuring atomicity when transferring money between accounts.

### **14. Replica**
#### **Real-World Use Case**: Setting up high availability for a distributed system.
