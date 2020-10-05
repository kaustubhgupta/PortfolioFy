from github import Github
import os
import sys
import json


git = Github(sys.argv[1])
print(f'Request left at start of the script: {git.rate_limiting}')
git_username = git.get_user().login


repo_list = [repo.name for repo in git.get_user().get_repos()]
data = {}

for repo in repo_list:
    print(f'Repo being checked: {repo}')
    try:
        repo_topics = git.get_repo(git_username + '/' + repo).get_topics()
        if len(repo_topics)!=0 and 'project' in repo_topics:
            data[f'{repo}'] = repo_topics
        else:
            continue
    except:
        continue

with open('data.json', 'w') as fp:
    json.dump(data, fp)

print(f'Request left at end of the script: {git.rate_limiting}')



