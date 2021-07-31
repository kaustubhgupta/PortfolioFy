# Action Parameters

These are the parameters that are used in the GitHub Action PortfolioFy as default whenever any user configures the action in their repo. Feel free to explore and play with these parameters. 

| Option         | Default Value | Description                                                                  | Required | Example |
| -------------- | ------------- | ---------------------------------------------------------------------------- | -------- | ------- |
| `gh_token`     | NA            | GitHub Personal Access token                                                 | Yes      |  NA     |
| `theme`        | `1`           | Level of the webpage you want to render: 1 or 2                                   | No       |  1      | 
| `blogs`        | `False`       | Include blogs in your Portfolio              | No       |  True   |
| `hackathons`   | `False`       | Include repositories that are tagged as `hackathon` topic | No       |  True |
| `stats_choice` | `1`           | Type/Style of GitHub stats you want to include. A total of 7 types of GitHub stats are available. See the sections below for more information     | No       |  6 |
| `stats_customization` | Comming Soon | Customize the GitHub stats chosen by passing additional parameters supported | Comming Soon | Comming Soon| 
| `social_links` | `False`       | Links for Linkedin, Twitter, Dev. to, Medium, or Stackoverflow can be included. All handles are not necessary, you can provide them as comma-separated list as per need in any order | No       | `'https://www.linkedin.com/in/kaustubh-gupta/, https://twitter.com/Kaustubh1828, https://medium.com/@kaustubhgupta1828, https://dev.to/kaustubhgupta, https://stackoverflow.com/users/14681298/kaustubh'`|
| `resume_link` | `False` | Link for resume uploaded online | No | `'https://drive.google.com/fnskaml...'` |
| `allow_footer` | `True` | Whether you want to display the credits of the creator at the end of the webpage | No | False |
| `project_sort_by` | `'stars'` | Control the sorting of projects by `'stars'` or `'forks'` | No | `'forks'` |


## `theme` (Theme Level)

There are two levels of the webpage that can be rendered using this action. They are numbered as 1 and 2. You can select any of the themes depending upon your usage.

### Theme 1

This is a basic level theme.

![](./images/gifpreviewL1.gif)

### Theme 2

This is an advanced theme provided by [Start Bootstrap](https://startbootstrap.com/theme/resume). It is fully interactive, good-looking, and more responsive on mobile devices.

![](./images/gifpreviewL2.gif)

## `hackathons` (Hackathons Entry)

Hackathon is an optional parameter to be included in the portfolio. By default, it is False but you can enable it in the workflow as shown below:

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            hackathons: True
```
## `stats_choice` (GitHub Stats)

You can choose from 7 types of stats generation. All of them are made by different creators and you will find the link to all of them so that you can customize them in the later version of this action. 

### 1

[Anurag Hazra](https://github.com/anuraghazra/github-readme-stats)'s GitHub Readme Stats

![](https://github-readme-stats.vercel.app/api?username=kaustubhgupta)

### 2

[Simon Lecoq](https://github.com/lowlighter/metrics)'s infographics generator with 30+ plugins and 100+ options to display stats about GitHub profile

![](https://metrics.lecoq.io/kaustubhgupta)

### 3

[Casper](https://github.com/vn7n24fzkq/github-profile-summary-cards)'s tool to generate Github summary card for profile README

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=kaustubhgupta)

### 4

[Jonah Lawrence](https://github.com/DenverCoder1/github-readme-streak-stats)'s contribution streak! 🌟 Display your total contributions, current streak, and longest streak on your GitHub profile README

![](https://github-readme-streak-stats.herokuapp.com/?user=kaustubhgupta)

### 5

[Joshua Clifford Reyes](https://github.com/LordDashMe/github-contribution-stats)'s Dynamically generated Github Contribution Stats. 📈 📆

![](https://github-contribution-stats.vercel.app/api/?username=kaustubhgupta)

### 6

[Ryota Sakamoto](https://github.com/ryo-ma/github-profile-trophy)'s dynamically generated GitHub Stat Trophies on your readme

![](https://github-profile-trophy.vercel.app/?username=kaustubhgupta)

### 7

[Vincent Voyer](https://github.com/vvo/sourcekarma)'s Discover how people react to you on GitHub 👍 

![](https://sourcekarma-og.vercel.app/api/kaustubhgupta/github)

_Note: This action requires you to freely sign-up for an account on source karma website. Visit [here](https://sourcekarma.vercel.app/)_

## `blogs` (Blogs Entry)

The blog is an optional parameter to be included in the portfolio. By default, it is False but you can enable it in the workflow as shown below:

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            blogs: True
```
This parameter, when enabled also requires you to configure blogpost-workflow. See the [advanced usage](./pages/Advanced-Usage.md) section for more information.

## `stats_customization` (GitHub stats Customization)

Coming Soon...

## `social_links` (Add Social Links)

You can add your social media handles to connect better with your audience. Currently, you can add links to Linkedin, Twitter, Dev. to, Medium, or Stackoverflow. There is no restriction to add all of them. You can skip this parameter, add partial links or all the links depending upon the usage!

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            social_links: 'https://www.linkedin.com/in/kaustubh-gupta/, https://twitter.com/Kaustubh1828, https://medium.com/@kaustubhgupta1828, https://dev.to/kaustubhgupta, https://stackoverflow.com/users/14681298/kaustubh'
```
## `resume_link` (Resume Link)

You can add the `View Resume` section in your portfolio by providing the link to the resume in this parameter. By default, it is false. 

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            resume_link: 'https://drive.google.com/fnskaml...'
```

## `allow_footer` (Allow Footer at the end)

This parameter allows you to control whether you want to display the credits of the creator at the end of the webpage. By default, it's true :)

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            allow_footer: False
```

## `project_sort_by` (Projects Sorting)

You can control how you want the projects listed under the `projects and hackathons` sections to be sorted. Two options/basis are available: `forks` & `stars`. 

```yml
.
.
.
- uses: actions/checkout@v2
        - uses: kaustubhgupta/PortfolioFy@main
          with:
            gh_token: ${{ secrets.TOKEN }} 
            projects_sort_by: 'forks'
```