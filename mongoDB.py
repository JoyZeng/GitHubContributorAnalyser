import pymongo

# get db with all params
def getDB(host, port, dbName):
    client = pymongo.MongoClient(host=host, port=port)
    # create automatically if not exist
    db = client[dbName]
    return db


#get collection with DB, collectionName
def getCollectionWithDB(db, collectionName):
    collection = db[collectionName]
    return collection


# save data
def saveData(collection, list):
    for item in list:
        # compare a new dictionary with the already exist one based on the id, if not exist, just insert it
        collection.update_one({"id": item["id"]}, {"$set": item}, upsert=True)


# get member list
def getMemberList(collection):
    list = []
    for i in collection.find():
        list.append(i)
    return list



# get a list of members' username
def getMemberUsernameList(collection):
    list = []
    for i in collection.find({}, {'login': 1, "_id": 0}):
        list.append(i["login"])
    return list



# get a list of user information
def getMemberInfoList(collection):
    list = []
    for i in collection.find():
        list.append(i)
    return list

# get a list of member location
def getMemberInfoLocationList(collection):
    list = []
    for i in collection.find({}, {"location":1, "_id":0}):
        list.append(str(i["location"]))
    return list











