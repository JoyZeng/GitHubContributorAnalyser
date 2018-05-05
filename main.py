import settings
import mongoDB
import request


def main():

    organization = "facebook"

    # save data to local mongoDB
    db = mongoDB.getDB(settings.MONGO_HOST, settings.MONGO_PORT, settings.MONGO_DB_GITHUB)
    memberCollection = mongoDB.getCollectionWithDB(db, settings.MONGO_COLLECTION_MEMBERS)
    memberInfoCollection = mongoDB.getCollectionWithDB(db, settings.MONGO_COLLECTION_MEMBERS_INFO)

    # get member list from internet
    memberList = request.getMemberListOfOrganization(organization)
    # save list to local mongoDB
    mongoDB.saveData(memberCollection, memberList)
    # get a list of member username
    list = mongoDB.getMemberUsernameList(memberCollection)

    # get member information list from internet
    infoList = request.getUserInformationList(list)
    # save list to local mongoDB
    mongoDB.saveData(memberInfoCollection, infoList)


main()
