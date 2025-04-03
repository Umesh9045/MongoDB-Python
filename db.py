
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://umesh9045:umesh9045@clustertest.nhv65gr.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    # Select database and collection
    db = client.payment_gateway_test     # db = Database Name
    users_collection = db["users"]       # Collection Name
    payments_collection = db["payments"] # Collection Name
    refunds_collection = db["refunds"]

except Exception as e:
    print(e)