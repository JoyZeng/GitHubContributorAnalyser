import operator
import csv
import mongoDB

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
    #print(dict)
    for item in array:
        data = {}
        data["City"] = item[0]
        data["Count"] = item[1]
        rows.append(data)
    with open(fileName, "w") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(rows)





