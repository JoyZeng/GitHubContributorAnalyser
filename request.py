import requests
import json
import settings

# get organization member list
def getMemberListOfOrganization(organization):
    memberList = []
    page = 1
    list = getMemberList(organization, page)
    # keep getting data from API till there is no more data return back
    while len(list) != 0:
        memberList = memberList + list
        page = page + 1
        list = getMemberList(organization, page)
    return memberList


# get organization member list with extract page
def getMemberList(organization, page):
    url = settings.organizationUrl(organization) \
          + "/members?access_token=" \
          + settings.TOKEN \
          + "&page=" \
          + str(page)
    r = requests.get(url, timeout=60)
    list = json.loads(r.text)
    return list

#get user information list based on a name list
def getUserInformationList(list):
    infoList = []
    for name in list:
        userInfo = getUserInformation(name)
        infoList.append(userInfo)
    return infoList


# get user information with username
def getUserInformation(userName):
    print(userName)
    url = settings.GITHUB_API_HOST + "/users/" + userName + "?access_token=" + settings.TOKEN
    print(url)
    r = requests.get(url, timeout=60)
    data = json.loads(r.text)
    return data

