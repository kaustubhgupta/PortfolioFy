import re


class Convertors:
    '''
    This class of functions contains all the additional functions required to convert the data into
    HTML components for website.
    '''

    def __init__(self):
        pass

    def soicalLinksListToHTML(self, links_list: str, git_username: str) -> str:
        '''
        Function to convert the list of all the social links to HTML tags "a href" with appropriate icons. 
        '''

        links_data = {}
        platforms = ['medium', 'linkedin', 'twitter', 'dev', 'stackoverflow']

        if 'false' in links_list:
            return f'<a href="https://www.github.com/{git_username}"><img width="55px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" /></a><span style="display:inline-block; width: 10px;"></span>'
        else:
            for platform in platforms:
                for link in links_list:
                    if re.search(platform, link) is not None:
                        links_data[platform] = link

            htmlData = ''

            for social_platform, user_link in links_data.items():
                if social_platform == 'dev':
                    htmlData += f'<a href="{user_link}"><img width="55px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/dev-dot-to.svg" /></a><span style="display:inline-block; width: 10px;"></span>'
                else:
                    htmlData += f'<a href="{user_link}"><img width="55px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/{social_platform}.svg" /></a><span style="display:inline-block; width: 10px;"></span>'

            htmlData += f'<a href="https://www.github.com/{git_username}"><img width="55px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" /></a><span style="display:inline-block; width: 10px;"></span>'
            return htmlData

    def repoDataToHTML(self, data: dict, git_username: str) -> str:
        '''
        Function to convert the repository data (title, topics, forks, stars, description) into GitHub looking repository view.
        All repositories will be clubbed together.
        '''

        repositoresHTML = ''

        if len(data) != 0:
            count_project = 1

            temp = dict(sorted(data.items(),
                               key=lambda x: x[1]['repo_stars']))

            projects_names = list(temp.keys())[::-1]

            for project in projects_names:
                topics = ''

                for topic in data[project]['repo_topics']:
                    topics += f'''<button class="button"><text class="button-text">{topic}</text></button>'''

                repositoresHTML += f'''<div class="div-repos" align="left" id="{count_project}">
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

        return repositoresHTML
