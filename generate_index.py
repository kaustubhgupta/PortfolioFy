from github import Github
from themes.level_1.level1 import genHTMLLevel1
from themes.level_2.level2 import genHTMLLevel2
from functions.RepoToHTML import repotohtml
from distutils.util import strtobool
import sys
import json
import os

git = Github(sys.argv[1])
theme_selected = sys.argv[2]
blogs = strtobool(sys.argv[3])
include_hackathon = strtobool(sys.argv[4])
stats_choice = sys.argv[5]
start = git.rate_limiting[0]
print(f'Request left at start of the script: {start}')

user_object = git.get_user()
git_username = user_object.login
user_data = {'username': git_username,
             'git_photo_url': user_object.avatar_url,
             'git_bio': user_object.bio,
             'git_email': user_object.email,
             'git_followers': user_object.followers,
             'git_following': user_object.following,
             'name': user_object.name,
             'latest_updated': str(user_object.updated_at)}

repo_list = [repo.name for repo in git.get_user().get_repos()]
project_data = {}
hackathon_data = {}

if include_hackathon:
    for repo in repo_list:
        print(f'Repo being checked: {repo}')
        try:
            repo_object = git.get_repo(git_username + '/' + repo)
            repo_topics = repo_object.get_topics()
            if len(repo_topics) != 0:
                if 'project' in repo_topics:
                    project_data[f'{repo}'] = {'repo_topics': repo_topics,
                                               'repo_description': repo_object.description,
                                               'repo_stars': int(repo_object.stargazers_count),
                                               'repo_forks': int(repo_object.forks_count)}

                if 'hackathon' in repo_topics:
                    hackathon_data[f'{repo}'] = {'repo_topics': repo_topics,
                                                 'repo_description': repo_object.description,
                                                 'repo_stars': int(repo_object.stargazers_count),
                                                 'repo_forks': int(repo_object.forks_count)}

                else:
                    continue
            else:
                continue
        except:
            continue
else:
    for repo in repo_list:
        print(f'Repo being checked: {repo}')
        try:
            repo_object = git.get_repo(git_username + '/' + repo)
            repo_topics = repo_object.get_topics()
            if len(repo_topics) != 0:
                if 'project' in repo_topics:
                    project_data[f'{repo}'] = {'repo_topics': repo_topics,
                                               'repo_description': repo_object.description,
                                               'repo_stars': int(repo_object.stargazers_count),
                                               'repo_forks': int(repo_object.forks_count)}
                else:
                    continue
            else:
                continue
        except:
            continue


end = git.rate_limiting[0]
print(f'Request left at end of the script: {end}')
print(f'Requests Consumed in this process: {start - end}')

project_repos = repotohtml(project_data, git_username)
if include_hackathon:
    hackathon_repos = repotohtml(hackathon_data, git_username)
else:
    hackathon_repos = None

if theme_selected == '1':
    indexFile = genHTMLLevel1(
        user_data, project_repos, hackathon_repos, blogs, stats_choice)

elif theme_selected == '2':
    indexFile = genHTMLLevel2(user_data, project_repos,
                              hackathon_repos, blogs, stats_choice)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(indexFile)
