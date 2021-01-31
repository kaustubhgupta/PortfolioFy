### Various Parameters

These are the parameters that are passed in the GitHub Actions when any user configures this in their repo.

| Option         | Default Value | Description                                                                  | Required | Example |
| -------------- | ------------- | ---------------------------------------------------------------------------- | -------- | ------- |
| `gh_token`     | NA            | GitHub Personal Access token                                                 | Yes      |  NA     |
| `theme`        | `1`           | Type of webpage you want to render: 1 or 2                                   | No       |  1      | 
| `blogs`        | `False`       | Whether you want to include blogs in your Portfolio (True/False)             | No       |  True   |
| `hackathons`   | `False`       | Apart from Personal projects you can include hackathon projects (True/False) | No       |  True
| `stats_choice` | `1`           | Which type of GitHub stats you want to display in your profile: 1 or 2       | No       |  2
| `social_links` | `False`       | You can add social links for Linkedin, Twitter, Dev.to, Medium. Pass it as string of all the links | No       | 'https://www.linkedin.com/in/kaustubh-gupta/, https://twitter.com/Kaustubh1828, https://medium.com/@kaustubhgupta1828, https://dev.to/kaustubhgupta, https://stackoverflow.com/users/14681298/kaustubh'|

#### 1. GitHub Token (`gh_token`)
This token is the main entry point of authentication to GitHub to fetch the data required for building the website.

#### 2. Theme Level (`theme`)
Currently, there are two levels of the webpage that can be rendered using this action. They are numbered numerically as 1 and 2. 

#### 3. Blogs Entry (`blogs`)
This is an optional parameter that controls whether you want to include the latest blogs on your webpage. If selected True, a separate section will be created. 

#### 4. Hackathons Entry (`hackathons`)
This is an optional parameter that controls whether you want to include the hackathons you participated in on your webpage. If selected True, a separate section will be created.

#### 5. Statistics Choice (`stats_choice`)
This is an optional parameter that controls which type of stats you want to display on your webpage. Currently, there are two types numbered 1 and 2.

#### 6. Social Media Links (`social_links`)
This is the optional parameter that controls the display of social media icons on the webpage. Currently Linkedin, Twitter, Dev.to, Medium, and Stackoverflow is supported. The parameter takes in all the links as a single string.