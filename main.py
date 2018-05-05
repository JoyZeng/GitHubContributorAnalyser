import requests
import json
import settings
import mongoDB

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
    # save data to local mongoDB
    mongoDB.saveData(settings.MONGO_HOST, settings.MONGO_PORT, settings.MONGO_DB_GITHUB, settings.MONGO_COLLECTION_FACEBOOK_MEMBERS, memberList)


main()
