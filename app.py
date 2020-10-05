from github import Github
import os
import sys
'''
exceptions : github.GithubException.UnknownObjectException
'''

g = Github(sys.argv[1])
repo_list = [repo.name for repo in g.get_user().get_repos()]
print(g.get_repo('kaustubhgupta/' + str(repo_list[-3])).get_topics())
with open('test.txt', 'w') as f:
    f.write(str(g.get_repo('kaustubhgupta/' + str(repo_list[-3])).get_topics()))


