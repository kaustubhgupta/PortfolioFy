![PortfolioFy](https://socialify.git.ci/kaustubhgupta/PortfolioFy/image?description=1&font=KoHo&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Light) 
<p align="center">
<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white" align="center">
<img src="https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white" align="center">
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white" align="center">
<img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white "align="center">
</p>

Developers create hundreds of repositories, and hardly a few of them are presentable and showcased on social media/LinkedIn. This GitHub action allows you to generate your self-updating portfolio consisting of Projects, Hackathons, or maybe the latest Blogs.

<p align="center">
<img src="./images/combinedPreview.png" align="center">
</p>

An index file is pushed by this action which with the help of GitHub pages can be deployed as soon as it is committed to the repository. If you write blogs, then you can add [Blog Post Workflow](https://github.com/marketplace/actions/blog-post-workflow) to the main workflow for updating your portfolio. !

## Getting Your Profile Ready

- The repositories need to have `project`  topic to add to the project section and `hackathon` topic to add them in the hackathon section. If you add both the topics to the same repository then it will be reflected in both sections!

- A GitHub personal access token will be needed which can be obtained by going to Settings > Developer Settings > Personal Access Tokens.
  <div align="center"> <img src="./images/config.PNG" align="center"> </div>

_Note: If you give personal repositories access then they will be added to the sections but their links will not work_

## Repository Setup

GitHub actions can be integgrated in any repository. Create a new folder called `.github/workflows/<any-name>.yml`. Paste the following starter code:

```yml
name: Latest portfolio
on:
  schedule:
    - cron: '0 0 * * *'
    # This makes the action to run at the end of every day. Customize this accordingly or you can also trigger this action for GitHub events (Pull, Push). Check GitHub actions page for that.
  workflow_dispatch:

jobs:
  updating-portfolio:
    name: update-index-with-project
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: kaustubhgupta/PortfolioFy@main 
        with:
          gh_token: ${{ secrets.TOKEN }} # Create a secret to store the access token 
```

## Available Options
(To know more about each parameter, jump to [this](https://kaustubhgupta.github.io/PortfolioFy/#/./pages/Git-Actions-Parameters) page in documentation)

| Option         | Default Value | Description                                                                  | Required | Example |
| -------------- | ------------- | ---------------------------------------------------------------------------- | -------- | ------- |
| `gh_token`     | NA            | GitHub Personal Access token                                                 | Yes      |  NA     |
| `theme`        | `1`           | Level of webpage you want to render: 1 or 2                                   | No       |  1      | 
| `blogs`        | `False`       | Include blogs in your Portfolio              | No       |  True   |
| `hackathons`   | `False`       | Include repositories that were part of hackathon | No       |  True
| `stats_choice` | `1`           | Type of GitHub stats: 1 or 2       | No       |  2
| `social_links` | `False`       | Links for Linkedin, Twitter, Dev.to, Medium, and Stackoverflow.  | No       | 'https://www.linkedin.com/in/kaustubh-gupta/, https://twitter.com/Kaustubh1828, https://medium.com/@kaustubhgupta1828, https://dev.to/kaustubhgupta, https://stackoverflow.com/users/14681298/kaustubh'|
| `resume_link` | `False` | Link for resume pdf uploaded online | False | 'https://drive.google.com/fnskaml' |
| `allow_footer` | `True` | Whether you want to display the credits of the creator the end of the webpage | False | False |

## Regarding Blog Updates

There is an action called [Blog Post Workflow](https://github.com/marketplace/actions/blog-post-workflow). You can easily integrate this in your workflow via this template: (Highly recommended!)

```yml
name: Latest blog post workflow
on:
  push: # Every time index.html is pushed, this action runs and updates the blogs section!

jobs:
  update-readme-with-blog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: gautamkrishnar/blog-post-workflow@master
        with:
          feed_list: <Your feedlist>
          max_post_count: <Your Choice>
          readme_path: index.html
          template: "<h2 class='h2-blog'><a class='a-lightblue' href=$url>$title</a></h2>" # It is suggested not to modify this
          gh_token: ${{ secrets.TOKEN }}
```

Make sure to enable the blogs parameter in the main workflow:

```yml
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }}
            blogs: True
```

## Examples
- [My Portfolio](https://kaustubhgupta.github.io/)
- [My Workflow File](https://github.com/kaustubhgupta/kaustubhgupta.github.io/blob/master/.github/workflows/website.yml)
- [My Blogs Workflow File](https://github.com/kaustubhgupta/kaustubhgupta.github.io/blob/master/.github/workflows/blog.yml)

## Documentation
The detailed documentation for this project is available [here](https://kaustubhgupta.github.io/PortfolioFy)

## Happy?? Do Star ⭐ this Repo. 🤩

## Special Mentions

- [Anurag Hazra](https://github.com/anuraghazra/github-readme-stats) (GitHub stats)
 
- [Simon Lecoq](https://github.com/lowlighter/metrics) (GitHub stats)
- [Gautam Krishna R](https://github.com/marketplace/actions/blog-post-workflow) (Blogpost Action)
- [Test Room 7](https://github.com/marketplace/actions/update-files-on-github) (Git action for Commiting files to Repository)
- [Start Bootstrap](https://startbootstrap.com/theme/resume) (Amazing themes)

## License

[![MIT Licence](https://img.shields.io/github/license/kaustubhgupta/PortfolioFy)](https://choosealicense.com/licenses/mit/)
