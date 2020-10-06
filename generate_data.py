from github import Github
import sys
import json


git = Github('2f722e9b831a30ef658aeb491ba443d6d13e22da')
print(f'Request left at start of the script: {git.rate_limiting}')

user_object = git.get_user()
git_username = user_object.login
data_user = {'username': git_username,
            'git_photo_url': user_object.avatar_url, 
            'git_bio': user_object.bio, 
            'git_email': user_object.email, 
            'git_followers': user_object.followers,
            'git_following': user_object.following,
            'name': user_object.name,
            'latest_updated': str(user_object.updated_at)}

repo_list = [repo.name for repo in git.get_user().get_repos()]
data_project = {}
data_hackathon = {}

for repo in repo_list:
    print(f'Repo being checked: {repo}')
    try:
        repo_object = git.get_repo(git_username + '/' + repo)
        repo_topics = repo_object.get_topics()
        if len(repo_topics)!=0:
            if 'project' in repo_topics:
                data_project[f'{repo}'] = {'repo_topics': repo_topics,
                                         'repo_description':repo_object.description, 
                                         'repo_stars': repo_object.stargazers_count,
                                         'repo_forks': repo_object.forks_count }
            if 'hackathon' in repo_topics:
                data_hackathon[f'{repo}'] = {'repo_topics': repo_topics,
                                         'repo_description':repo_object.description, 
                                         'repo_stars': repo_object.stargazers_count,
                                         'repo_forks': repo_object.forks_count }
            else:
                continue
        else:
            continue
    except:
        continue


with open('data_user.json', 'w') as fp:
    json.dump(data_user, fp)

with open('data_project.json', 'w') as fp:
    json.dump(data_project, fp)

with open('data_hackathon.json', 'w') as fp:
    json.dump(data_hackathon, fp)

print(f'Request left at end of the script: {git.rate_limiting}')



