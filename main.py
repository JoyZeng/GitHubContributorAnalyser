import requests
import json
import pymongo
import settings

# get organization member list from GitHub API
def getMemberList(organization, page = 1):
    url = settings.organizationUrl(organization) \
          + "/members?access_token=" \
          + settings.TOKEN \
          + "&page=" \
          + str(page)
    r = requests.get(url, timeout = 60)
    list = json.loads(r.text)
    return list

# save data to local mongoDB
def saveData(list):
    client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
    db = client[settings.MONGO_DB]
    collection = db[settings.MONGO_COLLECTION]
    for item in list:
        collection.insert(item)


def main():
    memberList = []
    organization = "facebook"
    page = 1
    list = getMemberList(organization, page)
    # keep getting data from API till there is no more data return back
    while len(list) != 0:
        memberList = memberList + list
        page = page + 1
        list = getMemberList(organization, page)
    #save data
    saveData(memberList)


main()
