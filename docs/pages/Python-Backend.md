# generate_index.py

This file is the entry point of this action. It takes in the inputs for [parameters](./pages/Git-Actions-Parameters) and depending upon that passes the data to the HTML renders.

# themes/level_{num}

Every level folder contains one init and level_{num} file. The level file renders the actual HTML. The function takes in the user data, project repos, hackathon repos, blogs state, and stats choice. The hackathon repos are converted only if the state is True else None.

# functions/RepoToHtml.py

This is the function that takes in the repo data and user's username to convert it to HTML tags data. This returns a string of all the eligible repos in HTML form. The HTML, CSS tags, and their classes will remain the same for all levels.

# functions/addBlogs.py

This file contains all levels of blog entry functions. As this is an optional parameter, it will be called in the themes/level_{num}/level(num) file when the state selected by the user is True. If selected True, the comment present in the HTML file: `<!-- BLOG-ENTRY -->` needs to be replaced with the blogs section HTML which will only have the title and the div tag holding the comment `<!-- BLOG-POST-LIST:START --> <!-- BLOG-POST-LIST:END -->`. This comment is important as this will be used by other actions to insert the blogs. If you are implementing a navigation bar, then that blog header can be enabled by using another comment section as used as a level 2 theme. Here you are free to customize the CSS and HTML tags.

# functions/addHackathon.py

It has the same functionality as addBlogs.py. The only difference is of replacement comment: `<!-- HACKATHON-ENTRY -->`. You are free to customize the CSS and HTML tags here.

# functions/addSocialLinks.py

This function takes in the social_links parameter and converts it into the HTML code. The HTML code contains the link to that particular social platform with the associated logo. The function checks for the platform and assigns the key as that platform and value as the link. The check is done via regular expressions.

# functions/addResume.py
It has the same functionality as addBlogs.py. The only difference is of replacement comment: `<!-- RESUME-ENTRY -->`. 

# functions/addFooter.py
It has the same functionality as addBlogs.py. The only difference is of replacement comment: `<!-- FOOTER-ENTRY -->`.