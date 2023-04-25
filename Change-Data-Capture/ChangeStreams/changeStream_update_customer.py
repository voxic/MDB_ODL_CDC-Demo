import pymongo

# Set up the MongoDB Atlas connection string
connection_string = "mongodb+srv://<mongodb cluster>"

# Create a MongoDB client instance
client = pymongo.MongoClient(connection_string)

# Access the ODL database
db = client.ODL

# Access the customers_landing and customers collections
customers_landing = db.customers_landing
customers = db.customers

# Set up a MongoDB change stream to watch for new documents
with customers_landing.watch() as stream:
    print("Watching the 'customers_landing' collection...")
    for change in stream:
        # Get the new document that was inserted
        if change["operationType"] == "insert":
            new_doc = change["fullDocument"]
            
            # Construct a new document for the customers collection
            new_customer = {
                "customer_firstname": new_doc["payload"]["after"]["customer_firstname"],
                "customer_lastname": new_doc["payload"]["after"]["customer_lastname"],
                "customer_id": new_doc["payload"]["after"]["customer_id"]
            }
            
            # Update the customers collection with the new customer document
            customers.update_one(
                {"customer_id": new_customer["customer_id"]},
                {"$set": new_customer},
                upsert=True
            )
            
            print("Customer added or updated in 'customers' collection:", new_customer)

