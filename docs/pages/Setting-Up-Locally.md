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

_Note: For `current_repo_path`, `stats_customization`, and `current_repo_branch`, input any random string. These parameters are disabled for local testing file. Stats customization is under development_

Example case: 

```bash
python localTestingFile.py fknkfnnds 1 true true 3 dadas dsd 'https://drive.google.com/file/d/jfksdnfkdsn' true 'forks', dnsas, "https://www.linkedin.com/in/kaustubh-gupta/, https://twitter.com/Kaustubh1828, https://medium.com/@kaustubhgupta1828"
```

- The index file will be generated and now you can make changes to improve upon the webpage.