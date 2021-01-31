### Local Setup

- Setup up Git on your local system and clone this project. See the [contribution guide](https://github.com/kaustubhgupta/PortfolioFy/wiki/Contribution-Guide) for a detailed explanation.
- Make sure Python is installed.
- Create a separate environment to install the dependencies or you can skip this part if you can manage the packages of your own.
- For dependencies,
  ```python
  pip install -r requirements.txt
  ```
### Local Run

- As this is a GitHub Action, it will assume some [parameters](https://github.com/kaustubhgupta/PortfolioFy/wiki/Git-Actions-Parameters) to be passed before running the script.
- To successfully run this:
  ```python
  python generate_index.py <GITHUB_TOKEN> <THEME_LEVEL> <BLOGS_COND> <HACKATHHONS_COND> <STATS_CHOICE>
  ```
- The index file will be generated and now you can make changes to improve upon the webpage

Read more about the [parameters here](https://github.com/kaustubhgupta/PortfolioFy/wiki/Git-Actions-Parameters).


