import pymongo

# Set up the MongoDB Atlas connection string
connection_string = "mongodb+srv://<mongodb cluster>"

# Create a MongoDB client instance
client = pymongo.MongoClient(connection_string)

# Access the ODL database
db = client.ODL

# Access the accounts_landing and customers collections
accounts_landing = db.accounts_landing
accounts = db.accounts

# Set up a MongoDB change stream to watch for new documents
with accounts_landing.watch() as stream:
    print("Watching the 'accounts_landing' collection...")
    for change in stream:
        # Get the new document that was inserted
        if change["operationType"] == "insert":
            new_doc = change["fullDocument"]
            
            # Construct a new document for the customers collection
            new_account = {
                "account_id": new_doc["payload"]["after"]["account_id"],
                "account_type": new_doc["payload"]["after"]["account_type"],
                "balance": new_doc["payload"]["after"]["balance"],
                "customer_id": new_doc["payload"]["after"]["customer_id"]
            }
            
            # Update the customers collection with the new customer document
            accounts.update_one(
                {"account_id": new_account["account_id"]},
                {"$set": new_account},
                upsert=True
            )
            
            print("Account added or updated in 'accounts' collection:", new_account)

