# FastAPI + MongoDB (Serverless Architecture) Project Setup

## 📂 Project Structure
```
project_root/
│
│--routes/     
│   │-- users.py        # Routes all user related apis
│   │-- payments.py     # Routes all payment related apis
│--services/
│   │-- users.py        # All users related functions that trigger by apis
│   │-- payments.py     # All payments related functions that trigger by apis
│-- models.py           # Validation for data input for apis
│-- db.py               # Database and collection configuration
│-- main.py             # Start file (origin)
│-- requirements.txt
│-- readme.md
```

---

## 🚀 Setup Instructions

### **1️⃣ Install Python & Virtual Environment**
Ensure you have **Python 3.8+** installed. Then, create a virtual environment:
```sh
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **2️⃣ Install Dependencies**
Run the following command to install the required packages:
```sh
pip install -r requirements.txt
```

#### **requirements.txt**
```
fastapi
uvicorn
pymongo
motor
``` 

### **3️⃣ Configure MongoDB Connection**
Edit the `db.py` file and replace the `uri` with your MongoDB connection string.
```python
from motor.motor_asyncio import AsyncIOMotorClient

uri = "your_mongodb_uri_here"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["your_database_name"]
users_collection = db["users_collection_name"]
payments_collection = db["payments_collection_name"]
```

### **4️⃣ Run the FastAPI Server**
Start the server using Uvicorn:
```sh
uvicorn main:app --reload
```

Server will run at: `http://127.0.0.1:8000`

### **5️⃣ API Endpoints**
#### **User APIs**
- **Create User** → `POST /users`
- **Get Users** → `GET /users`

#### **Payment APIs**
- **Create Payment** → `POST /payments`
- **Get Payments** → `GET /payments`

### **6️⃣ Test API with Swagger UI**
Once the server is running, visit:
- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### ✅ **Project is now set up and ready to use!** 🚀