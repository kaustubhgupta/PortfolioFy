# generate_index.py

This file is the entry point of this action. It takes in the inputs for [parameters](./pages/Git-Actions-Parameters) and depending upon that passes the data to the HTML renders.

# themes/level_{num}

Every level folder contains one `init` and `level_{num}` file. The level file renders the actual HTML. The function takes in all the required data and generates the basic HTML structure.

# utils/adders.py
This class of functions contains all the additional functions required to add the website components.

- **Adder/addBlogsL1()**
Function to add blogs section and meta text (comment) needed for blogpost workflow in level 1 theme.

- **Adder/addBlogsL2()**
Function to add blogs section and meta text (comment) needed for blogpost workflow in level 2 theme.  For theme 2, the "Blogs" section needed to be added both in Menu (Navigation) bar and the main section  

- **Adder/addFooter()**
Function to add creator credits at the end of the webpage generated. 

- **Adder/addHackathonL1()**
Function to add hackathons data in level 1 theme.

- **Adder/addHackathonL2()**
Function to add hackathons data to level 2 theme. Here, the navigation menu also needs to be updated for the hackathon section.

- **Adder/addResumeL1()**
Function to add "View Resume" hyperlink in level 1 theme

- **Adder/addResumeL2()**
Function to add "View Resume" hyperlink in level 2 theme

- **Adder/addGitHubStats()**
Function to add GitHub stats. Different choices will be available for each stat. Stats can be customized.

# utils/convertors.py
This class of functions contains all the additional functions required to convert the data into
HTML components for website.

- **Convertors/soicalLinksListToHTML()** 
Function to convert the list of all the social links to HTML tags "a href" with appropriate icons.

- **Convertors/repoDataToHTML()** 
Function to convert the repository data (title, topics, forks, stars, description) into GitHub-looking repository view. All repositories will be clubbed together. The sorting parameter controls the arrangement of the project according to stars or forks.