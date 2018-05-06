import operator
import csv

import mongoDB
import request
import requestUtil

# analyse the locations of the members
# save the ranked locations based on the most members to a csv file
def analyseLocations(collection):
    lst = mongoDB.getMemberInfoLocationList(collection)
    list = unifyLocation(lst)
    dict = {}
    for i in list:
        if i in dict.keys():
            val = dict[i] + 1
            dict[i] = val
        else:
            dict[i] = 1
    # form the most to the least, the members located at
    sortedArray = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    # save the array to a csv file
    saveDictToLocalCSVFile(sortedArray, "city.csv")



# unify location, for example London and Landon,England are the same place
def unifyLocation(list):
    lst = []
    for i in list:
        item = getFirstWord(i)
        lst.append(item)
    return lst

# get the city name
def getFirstWord(words):
    list = words.split(",")
    return list[0].strip()


def saveDictToLocalCSVFile(array, fileName):
    headers = ["City", "Count"]
    rows = []
    for item in array:
        data = {}
        data["City"] = item[0]
        data["Count"] = item[1]
        rows.append(data)
    with open(fileName, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(rows)



# the result will be like,
# [{"member": "a8m", "commits": [{"JavaScript": 167777}, {"Python": 899}, {"C++": 122}]},
# {"member": "﻿aaronabramov", "commits": [{"Java": 123444}, {"Go": 9}, {"C": 6},...]} ...]
# 167777 is the sum of a8m's JavaScript repos commit number
# rank the language based on the total commit number
# rank the member based on the total commits number
# then We can know what every member is good at
# I have not finished yet

# analyse members' ability, what they are good at
def anaylyseMembersAbility(collection):
    lst = mongoDB.getMemberInfoList(collection)
    for i in lst:
        # a member's login name
        userName = i["login"]
        # a member's repos url
        reposUrl = i["repos_url"]
        #analyse
        analyseMemberAbility(userName, reposUrl)
        count = count + 1

# analyse every member, what they are good at
def analyseMemberAbility(userName, reposUrl):
    # get a list of repos
    list = request.getUserReposList(reposUrl)
    #language commit count dict
    dict = {}
    # analyse every repo
    for i in list:
        # repo url
        repoUrl = i["contributors_url"]
        # repo language
        language = str(i["language"])
        # get a repo contributors list
        repoUrl = requestUtil.urlAppendToken(repoUrl)
        lst = requestUtil.getDataWithUrl(repoUrl)
        for contributor in lst:
            if str(contributor["login"]) == userName:
                val = contributor["contributions"]
                if language in dict.keys():
                    val = val + dict[language]
                dict[language] = val
                break

    dic = {}
    dic["member"] = userName
    dic["commits"] = dict
    print(dic)




