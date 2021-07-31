# Contributing to PortFolioFy
👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Contributions are always appreciated as **no contribution is too small.**
**We are here to learn and grow along with the community**


# Submitting Contributions
- **Perfom all the initials:** Fork the repo, clone your version locally, add upstream to my repo `https://github.com/kaustubhgupta/PortfolioFy`, create a new branch. If you're not aware of all these terminologies, there are ton of resources available on internet.

- **Choosing the Issue:** You can create issues for bugs, new features, documentation errors or anything you want to add. Open a new issue and we will have the discussion about it.

# Local Setup

- Setup up Git on your local system and clone this project. 
- Make sure Python is installed.
- Create a separate environment to install the dependencies or you can skip this part if you can manage the packages of your own.
- For dependencies
```python
pip install -r requirements.txt
```

# Local Run

- As this is a GitHub Action, it will assume some [parameters](./pages/Git-Actions-Parameters) to be passed before running the script.

- The GitHub action is dependent on some paths of the GitHub workspace and therefore, these cannot be passed to the script file while working locally.

- Also, you don't want your local changes to be pushed to your production repositories :)

- Therefore, you need to use `localtestingfile.py` which doesn't push the file to the repository. It only writes the index file to the root folder.  

- To successfully run this file, pass arguments as:
  ```python
 python localTestingFile.py <gh_token> <theme> <blogs> <hackathons> <stats_choice> <current_repo_path> <current_repo_branch> <resume_link> <allow_footer> <project_sort_by> <stats_customization> <social_links>
  ```

_Note: For `current_repo_path` and `current_repo_branch`, input any random string. These parameters are disabled for local testing file_

- The index file will be generated and now you can make changes to improve upon the webpage.


**Important:** Make sure to check the docs for more detailed descriptions of various parameters and files used.