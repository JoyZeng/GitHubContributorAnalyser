import requestUtil

# get organization member list
def getMemberListOfOrganization(organization):
    url = requestUtil.organizationMemberListUrl(organization)
    list = requestUtil.getList(url)
    return list


# get user information list based on a name list
def getUserInformationList(list):
    infoList = []
    for name in list:
        userInfo = getUserInformation(name)
        infoList.append(userInfo)
    return infoList


# get user information with username
def getUserInformation(userName):
    url = requestUtil.userInformationUrl(userName)
    data = requestUtil.getDataWithUrl(url)
    return data

# get a member's repos list
def getUserReposList(reposUrl):
    list = requestUtil.getList(reposUrl)
    return list











