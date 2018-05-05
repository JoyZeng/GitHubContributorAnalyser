TOKEN = "a0372c4fc803e4739a7edd5d66bb1e43db40e2de"

GITHUB_API_HOST = "https://api.github.com"

# host IP
MONGO_HOST = "127.0.0.1"
# port
MONGO_PORT = 27017
# database name
MONGO_DB_GITHUB = "github"
# collection name
MONGO_COLLECTION_MEMBERS = "members"
# collection name
MONGO_COLLECTION_MEMBERS_INFO = "members_information"

# get organization GitHub API
def organizationUrl(organization):
    return GITHUB_API_HOST + '/orgs/' + organization

