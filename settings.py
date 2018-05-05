TOKEN = "a0372c4fc803e4739a7edd5d66bb1e43db40e2de"

GITHUB_API_HOST = "https://api.github.com"

# host IP
MONGO_HOST = "127.0.0.1"
# port
MONGO_PORT = 27017
# database name
MONGO_DB = "github"
# collection name
MONGO_COLLECTION = "facebook_members"

# get organization GitHub API
def organizationUrl(organization):
    return GITHUB_API_HOST + '/orgs/' + organization

