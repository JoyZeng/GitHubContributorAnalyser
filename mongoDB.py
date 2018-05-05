import pymongo

# save data to local mongoDB
def saveData(host, port, dbName, collectionName, list):
    client = pymongo.MongoClient(host=host, port=port)
    # create automatically if not exist
    db = client[dbName]
    collection = db[collectionName]
    for item in list:
        # compare a new dictionary with the already exist one based on the id, if not exist, just insert it
        collection.update_one({"id": item["id"]}, {"$set": item}, True)





