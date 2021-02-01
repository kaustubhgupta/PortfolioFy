Do you want to contribute to this project but don't know how?

This documentation would help you during the process.
Contributions are always appreciated as **no contribution is too small.**
**We are here to learn and grow along with the community**

:warning: **Please refrain from plagiarising code for the sake of pull request. We highly discourage it. The contributions which involve plagiarism will not be merged.**

# Submitting Contributions

The following steps below outline how to make contributions to the existing project. All the images shown below are from another project but serve the purpose.

## Step 0: Find/Create an issue(any issue you can work on)

-   Take a look at any Existing Issue you could work on✨ or create your **own** Issues!💡
-   Wait for the `Issue` to be assigned to you, after which you can start working on it.
-   **Note: Every change in this project should/must have an associated issue.**

![issue](https://github.com/kaustubhgupta/PortfolioFy/blob/main/images/issue.jpg)

## Step 1: Fork the Project/Repository

-   Fork this Repository. This action will create a `Local Copy` of this Repository for you to work on your personal GitHub account. It is advised to keep a reference to the original project in the `upstream` remote.

Use terminal and write the following commands:

```
$ git clone https://github.com/<your-username>/<repo-name>
$ cd <repo-name>
$ git remote add upstream https://github.com/<upstream-owner>/<repo-name>
```

![fork](https://github.com/kaustubhgupta/PortfolioFy/blob/main/images/fork.jpg)

**Note:** You don't need to copy or type the dollar sign.

-   If you have already forked the project, update your copy before working.

```
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>
```

## Step 2: Create a Branch

Create a new branch. Use its name to identify the issue your addressing.

-   Type the following commands in your terminal to create a new branch. You could call it: Branch_Name and switch to that branch

```
$ git checkout -b <branch_name>

#for example
$ git checkout -b "contribution"
```

:warning: **Please refrain from making changes to the main branch, otherwise we'll be unable to merge your contribution**

## Step 3: Work on a specific issue

-   Only work on the issue(s) assigned to you, in this way code redundancy can be minimized and every effort would be able to make a change.
-   Only add the files/folders needed.
-   After you've made changes or made your contribution to the project, add changes to the branch you've just created by:

```
# To add all new files to branch Branch_Name

$ git checkout -b <branch_name>
$ git add .

#If you want to add individual files for example an index.html file you made changes to, write the command.

$ git checkout -b <branch_name>
$ git add index.html
```

This would add the file to the staging area.

## Step 4: Make a commit

-   To commit means to give a descriptive message that shows what you've modified:

```
# This message gets associated with all files you have added to the staging area through the git add command.

$ git commit -m "your commit message"
```

## Step 5: Work Remotely

-   Now, you are ready to push your work to the remote repository.
-   To setup the project locally, have a look at this (setting up guide)[https://kaustubhgupta.github.io/PortfolioFy/#/wiki/Setting-Up-Locally]
-   The next step would be to take the local version you've worked on, on your computer, and `push` it to GitHub.
-   The next step would be to take the local version you've worked on and push it to GitHub.

```
#To do that, write the following commands in your terminal

$ git push -u origin Branch_Name
```

-   Here's how it will look

![branch](https://github.com/kaustubhgupta/PortfolioFy/blob/main/images/branch.jpg)

-   So that is the branch you'd create. I named my contribution to addressing a particular issue, but it could be anything you want.

## Step 6: Compare Changes

-   You can compare the changes you've made in your branch with those in the main project. Just click on the compare button.

![compare](https://github.com/kaustubhgupta/PortfolioFy/blob/main/images/compare-changes.jpg)

## Step 7: Create a pull Request

-   Next step would be to create a pull request. 
-   Now wait for Mentors and Project admins to review your code and make changes if suggested!

![pull-request](https://github.com/kaustubhgupta/PortfolioFy/blob/main/images/pull-request.jpg)

And, you're done! Your pull request would get submitted.
It will be reviewed and merged as soon as possible.
Please check the reviews until your pull request is not merged, this will give you a better insight into the suggestions and improvements required(if any).

## In case you got stuck.

-   It might seem like a lot of it's your first time but everyone started new to GitHub and open source at some point. If you missed a few steps, don't worry, try again. You'd get better.
