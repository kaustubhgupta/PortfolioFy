import json

with open('data_user.json') as json_file:
    user_data = json.load(json_file)

with open('data_project.json') as json_file:
    project_data = json.load(json_file)

with open('data_hackathon.json') as json_file:
    hackathon_data = json.load(json_file)


css = '''
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
.img-rounded{
    border-radius: 50%;
}
'''

project_repos = ''
if len(project_data)!=0:
    count_project = 1
    projects_names = set(project_data.keys())
    for project in projects_names:
        topics = ''
        for topic in project_data[project]['repo_topics']:
            topics+= f'''<button class="button">{topic}</button>'''
        project_repos += f'''<div class="container">
        <div>
        <br>
        <h4 style='color:#0366d6'><a href="https://github.com/kaustubhgupta/{project}">{project}</a></h4>
        {topics}
        <br>
        <text style='color:#586069'>{project_data[project]['repo_description']}<text><br>
        </div>
        <img src="https://image.flaticon.com/icons/png/512/126/126482.png" width="16" height="16">{project_data[project]['repo_stars']}
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Octicons-repo-forked.svg/675px-Octicons-repo-forked.svg.png" width="16" height="16">{project_data[project]['repo_forks']}
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
            topics+= f'''<button class="button">{topic}</button>'''
        hackathon_repos += f'''<div class="container">
        <div>
        <br>
        <h4 style='color:#0366d6'><a href="https://github.com/kaustubhgupta/{hackathon}">{hackathon}</a></h4>
        {topics}
        <br>
        <text style='color:#586069'>{hackathon_data[hackathon]['repo_description']}<text><br>
        </div>
        <img src="https://image.flaticon.com/icons/png/512/126/126482.png" width="16" height="16">{hackathon_data[hackathon]['repo_stars']}
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Octicons-repo-forked.svg/675px-Octicons-repo-forked.svg.png" width="16" height="16">{project_data[project]['repo_forks']}
        <br>
        </div>  
        '''
        count_hackathon += 1


template = f'''
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
<style>{css}</style>
<body>
<div align="center">
<img class="img-rounded" align="center" alt="Image" height="250px" src="{user_data['git_photo_url']}" />
<h1 style='color:#f24b4b'> Hi, I am <a href="https://github.com/{user_data['username']}">{user_data['name']}</a>👨‍🎓 </h1>
<h6 style='color:#4a90ed'>{user_data['git_bio']}</h6>
<img  src="https://github-readme-stats.vercel.app/api?username={user_data['username']}&show_icons=true&theme=radical&count_private=true">
<h5 style='color:#697d3b'>Followers: <b>{user_data['git_followers']}</b>, Following: <b>{user_data['git_following']}</b></h5>
<br>
<h2 style="color:#d45131"> My Projects👇</h2>
<text style='font-size:16px'>(These repositories are tagged as project. *Updated: {user_data['latest_updated']})</text>
<div class="mx-auto my-auto" align="left">{project_repos}</div>
<br>
<h2 style="color:#d45131"> Hackathons I participated👇</h2>
<text style='font-size:16px'>(These repositories are tagged as Hackathon. *Updated: {user_data['latest_updated']})</text>
<div class="mx-auto my-auto" align="left">{hackathon_repos}</div>
<br>
<h2 style="color:#d45131"> My Latest Blogs✍️</h2>
<div class="mx-auto my-auto" align="left">
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
</div>
</body>
<footer>
<h6>Contact on Email: {user_data['git_email']}</h6>
</footer>
</div>
'''

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(template)