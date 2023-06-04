from github import Github
import os
from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("MANGO_TOKEN")

print(TOKEN)


# using an access token
g = Github("access_token")

print(g.get_user())

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

    