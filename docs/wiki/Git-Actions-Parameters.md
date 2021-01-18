### Various Parameters

These are the parameters that are passed in the GitHub Actions when any user configures this in their repo.

| Option         | Default Value | Description                                                     | Required |
| -------------- | ------------- | --------------------------------------------------------------- | -------- |
| `gh_token`     | NA            | GitHub Personal Access token                                    | Yes      |
| `theme`        | `1`           | Type of webpage you want to render                              | No       |
| `blogs`        | `False`       | Whether you want to include blogs in your Portfolio             | No       |
| `hackathons`   | `False`       | Apart from Personal projects you can include hackathon projects | No       |
| `stats_choice` | `1`           | Which type of GitHub stats you want to display in your profile  | No       |

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