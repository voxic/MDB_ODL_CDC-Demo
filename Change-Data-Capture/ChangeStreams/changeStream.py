import pymongo
import json

# Set up the MongoDB Atlas connection string
connection_string = "mongodb+srv://<mongodb cluster>"

# Create a MongoDB client instance
client = pymongo.MongoClient(connection_string)

# Access the ODL database
db = client.ODL

# Access the customers_landing collection
collection = db.customers_landing

# Set up a MongoDB change stream to watch for new documents
with collection.watch() as stream:
    print("Watching the 'customers_landing' collection...")
    for change in stream:
        # Print any new documents that are added to the collection
        if change["operationType"] == "insert":
            # Pretty-print the JSON document
            pretty_doc = json.dumps(change["fullDocument"]["payload"]["after"], indent=4)
            print(pretty_doc)
