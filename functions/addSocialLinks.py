import re
from distutils.util import strtobool

def LinkstoHTML(links_list, git_username):

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
