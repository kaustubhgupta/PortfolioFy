# Local Setup

- Setup up Git on your local system and clone this project. 
- Make sure Python is installed.
- Create a separate environment to install the dependencies or you can skip this part if you can manage the packages of your own.
- For dependencies,
  ```python
  pip install -r requirements.txt
  ```
# Local Run

- As this is a GitHub Action, it will assume some [parameters](./pages/Git-Actions-Parameters) to be passed before running the script.
- To successfully run this:
  ```python
  python generate_index.py <GITHUB_TOKEN> <THEME_LEVEL> <BLOGS_COND> <HACKATHHONS_COND> <STATS_CHOICE>
  ```
- The index file will be generated and now you can make changes to improve upon the webpage