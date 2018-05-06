import settings
import request
import mongoDB
import analyse



def main():

    # organization = "facebook"
    # # get member list from internet
    # memberList = request.getMemberListOfOrganization(organization)
    # # save list to local mongoDB
    # mongoDB.saveData(mongoDB.getMemberCollection(), memberList)
    # # get a list of member username
    # list = mongoDB.getMemberUsernameList(mongoDB.getMemberCollection())
    #
    # # get member information list from internet
    # infoList = request.getUserInformationList(list)
    # # save list to local mongoDB
    # mongoDB.saveData(mongoDB.getMemberInfoCollection(), infoList)
    #
    # analyse.analyseLocations(mongoDB.getMemberInfoCollection())


    analyse.anaylyseMembersAbility(mongoDB.getMemberInfoCollection())


main()
