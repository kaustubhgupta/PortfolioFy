from github import Github
import sys
import json


git = Github(sys.argv[1])
print(f'Request left at start of the script: {git.rate_limiting}')

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

for repo in repo_list:
    print(f'Repo being checked: {repo}')
    try:
        repo_object = git.get_repo(git_username + '/' + repo)
        repo_topics = repo_object.get_topics()
        if len(repo_topics)!=0:
            if 'project' in repo_topics:
                project_data[f'{repo}'] = {'repo_topics': repo_topics,
                                         'repo_description':repo_object.description, 
                                         'repo_stars': repo_object.stargazers_count,
                                         'repo_forks': repo_object.forks_count }
            if 'hackathon' in repo_topics:
                hackathon_data[f'{repo}'] = {'repo_topics': repo_topics,
                                         'repo_description':repo_object.description, 
                                         'repo_stars': repo_object.stargazers_count,
                                         'repo_forks': repo_object.forks_count }
            else:
                continue
        else:
            continue
    except:
        continue




print(f'Request left at end of the script: {git.rate_limiting}')

css = '''
html {
  font-family: "Lucida Sans", sans-serif;
}
.footer{
   left: 0;
   bottom: 0;
   width: 100%;
   background-color:white;
   color: black;
   text-align: center;
}

a {
        background-color: transparent;
        text-decoration: none;
}

.a-blue {
        color: #0366d6;
        background-color: transparent;
        text-decoration: none;
}

.a-lightblue {
        color:#208fd4;
        background-color: transparent;
        text-decoration: none;
}

.button {
        background-color: #f1f8ff;
        border: none;
        color: #0366d6;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 16px;
}

.img-rounded {
        border-radius: 50%;
        height: 350px;
}

.img-stats{
        height: 250px;
}

h1 {
        font-size: 250%;
}

h2 {
        font-size: 150%;
}

.h2-repo {
        font-size: 160%;
}

h3 {
        font-size: 140%;
}

.div-repos {
        width: 60%;
}

.div-blog{
        width: 57%;
}

.h2-blog{
        font-size: 120%;
}

.div-main {
        padding-top: 50px;
        padding-right: 30px;
        padding-bottom: 50px;
        padding-left: 80px;
        
}
.text-repo{
        font-size: 100%;
        color:#586069;
}
.text-info{
        font-size:100%; 
        color:#586069;
}
@media only screen 
and (min-device-width : 320px) 
and (max-device-width : 480px) {
/* Styles */
.div-repos{
        width: 100%;
}
h1{
        font-size: 150%;
}
h2{
        font-size: 70%;
}
.img-rounded {
        border-radius: 50%;
        height: 400px;
}
.img-stats{
        height: 330px;
}
h3 {
        font-size: 80%;
}
.text-info{
        font-size:50%; 
        color:#586069;
}
.text-repo{
        font-size: 140%;
        color:#586069;
}
.h2-repo {
        font-size: 150%;
}
.button-text{
        font-size: 180%;
}
.div-blog{
        width: 100%;
}
.h2-blog{
        font-size: 140%;
}
}
'''

project_repos = ''
if len(project_data)!=0:
    count_project = 1
    projects_names = set(project_data.keys())
    for project in projects_names:
        topics = ''
        for topic in project_data[project]['repo_topics']:
            topics+= f'''<button class="button"><text class="button-text">{topic}</text></button>'''
        project_repos += f'''<div class="div-repos" align="left" id={count_project}>
        <br>
        <h2 class="h2-repo"><a class="a-blue" href="https://github.com/kaustubhgupta/{project}">{project}</a></h2>
        {topics}
        <br>
        <text class="text-repo">{project_data[project]['repo_description']}<text><br>
        <img src="https://image.flaticon.com/icons/png/512/126/126482.png" width="14" height="14">{project_data[project]['repo_stars']}
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Octicons-repo-forked.svg/675px-Octicons-repo-forked.svg.png" width="14" height="14">{project_data[project]['repo_forks']}
        <br>
        </div>  
        '''
        count_project += 1


hackathon_repos = ''
if len(hackathon_data)!=0:
    count_hackathon = 1
    hackathon_names = set(hackathon_data.keys())
    for hackathon in hackathon_names:
        topics = ''
        for topic in hackathon_data[hackathon]['repo_topics']:
            topics+= f'''<button class="button"><text class="button-text">{topic}</text></button>'''
        hackathon_repos += f'''<div class="div-repos" align="left" id={count_hackathon}>
        <br>
        <h2 class="h2-repo"><a class="a-blue" href="https://github.com/kaustubhgupta/{hackathon}">{hackathon}</a></h2>
        {topics}
        <br>
        <text class="text-repo">{hackathon_data[hackathon]['repo_description']}<text><br>
        <img src="https://image.flaticon.com/icons/png/512/126/126482.png" width="14" height="14">{hackathon_data[hackathon]['repo_stars']}
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Octicons-repo-forked.svg/675px-Octicons-repo-forked.svg.png" width="14" height="14">{hackathon_data[hackathon]['repo_forks']}
        <br>
        </div>  
        '''
        count_hackathon += 1


template = f'''
<html>
<title>{user_data['name']} Portfolio</title>
<head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
<style>{css}</style>
</head>
<body>
<div class="div-main" align="center">
<img class="img-rounded" alt="Image" height="350px" src="{user_data['git_photo_url']}" />
<h1 style='color:#f24b4b'> Hi, I am <a href="https://github.com/{user_data['username']}">{user_data['name']}</a>👨‍🎓 </h1>
<h2 style='color:#21439e'>{user_data['git_bio']}</h2>
<img class="img-stats" src="https://github-readme-stats.vercel.app/api?username={user_data['username']}&show_icons=true&theme=radical&count_private=true">
<h3 style='color:#751878'>Followers: <b>{user_data['git_followers']}</b>, Following: <b>{user_data['git_following']}</b></h3>
<br>
<h1 style="color:#d45131"> My Projects👇</h1>
<text class="text-info">(These repositories are tagged as project. *Updated: {user_data['latest_updated']})</text>
<br>
{project_repos}
<br>
<h1 style="color:#d45131"> Hackathons I participated👇</h1>
<text class="text-info">(These repositories are tagged as project. *Updated: {user_data['latest_updated']})</text>
<br>
{hackathon_repos}
<br>
<h1 style="color:#d45131"> My Latest Blogs✍️</h1>
<div align='left' class="div-blog">
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
</div>
<h3 style="color:#9a08c7">Contact on Email: {user_data['git_email']}</h3>
</div>
<div class="footer">
<p class="text-info">Generated by <a href="https://github.com/kaustubhgupta">Kaustubh Gupta</a>, Stats Generation Credits: <a href="https://github.com/anuraghazra/github-readme-stats">github-readme-stats</a></p>
</div>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(template)
