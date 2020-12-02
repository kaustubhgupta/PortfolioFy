def repotohtml(data, git_username):
    project_repos = ''
    if len(data) != 0:
        count_project = 1
        temp = dict(sorted(data.items(),
                           key=lambda x: x[1]['repo_stars']))
        projects_names = list(temp.keys())[::-1]
        for project in projects_names:
            topics = ''
            for topic in data[project]['repo_topics']:
                topics += f'''<button class="button"><text class="button-text">{topic}</text></button>'''
            project_repos += f'''<div class="div-repos" align="left" id={count_project}>
            <br>
            <h2 class="h2-repo"><a class="a-blue" href="https://github.com/{git_username}/{project}">{project}</a></h2>
            {topics}
            <br>
            <text class="text-repo">{data[project]['repo_description']}<text><br>
            <img src="https://image.flaticon.com/icons/png/512/126/126482.png" width="14" height="14">{data[project]['repo_stars']}
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Octicons-repo-forked.svg/675px-Octicons-repo-forked.svg.png" width="14" height="14">{data[project]['repo_forks']}
            <br>
            </div>  
            '''
            count_project += 1

    return project_repos
