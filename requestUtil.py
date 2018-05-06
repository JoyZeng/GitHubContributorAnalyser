import requests
import json

import settings


# get data with url
def getDataWithUrl(url):
    r = requests.get(url, timeout=60)
    data = json.loads(r.text)
    return data

# append access token to a url
def urlAppendToken(url):
    url = url + "?access_token" + settings.TOKEN
    return url

# append page to url
def urlAppendPage(url, page):
    url = url + "&page=" + str(page)
    return url


# get a list all the data till there is no more data
# GitHub API will return a list of data in page 1
def getList(url):
    url = urlAppendToken(url)
    list = []
    page = 1
    lst = getDataWithUrl(urlAppendPage(url, page))

    if isinstance(lst, dict):
        print("rate limited API GitHub ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("rate limited API GitHub ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return list
    while len(lst) != 0:
        list = list + lst
        page = page + 1
        lst = getDataWithUrl(urlAppendPage(url, page))
    return list

# get organization GitHub API
def organizationUrl(organization):
    return settings.GITHUB_API_HOST + '/orgs/' + organization


# url for getting organization member list
def organizationMemberListUrl(organization):
    url = organizationUrl(organization) + "/members?"
    return url

# url for getting user information
def userInformationUrl(userName):
    url = settings.GITHUB_API_HOST + "/users/" + userName
    url = urlAppendToken(url)
    return url





