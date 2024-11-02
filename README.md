# TDS 24T3 Project-1

Retrieval and analysis of GitHub users and their repositories.

## Project Structure

1. `users.csv`: Data of 301 GitHub users based in the city of London with over 500 followers.
2. `repositories.csv`: Data of 37,922 public repositories of these users, top 500 each by most recently pushed.
3. `fetch.py`: The Python script used to collect this data.
4. `fetch.json`: A JSON file containing fetch statistics.
5. `queries`: This directory contains GraphQL queries used to fetch data from GitHub API.
6. `analysis.ipynb`: A Jupyter notebook containing the analysis of the data.
7. `answers.ipynb`: Contains answers to the project assignment questions.
8. `.gitignore`: A file to exclude certain files from being tracked by Git.
9. `README.md`: This file. A summary of the project and its findings.

## How the Data was Sourced and Processed

- The data for this project was collected using GitHub's GraphQL API, which gives fine-grained control over the fields to fetch.
- Python scripts were used to get data from the API and processed it to extract user profiles and repository details.
- The information was saved in CSV files for easy retrieval and subsequent analysis.
- The cleaning step included standardizing company names—removing extra spaces, symbols like `@`, and making everything uppercase for consistency.
- One key challenge was handling rate limits from the GitHub API. This was mitigated by using the much more efficient GraphQL API.
- An interesting observation was that the search query, intended to fetch user data, occasionally returned empty `{}` responses. Upon further investigation, it was discovered that these entries corresponded to organizations rather than individual users.

## The Most Interesting and Surprising Facts

1. **Popularity and Repository Count**: Developers who create more public repositories usually have more followers. Each additional repository adds, on average, around 1.5 followers.

2. **Company Affiliation**: Most developers in London who are on GitHub work for Facebook.

3. **Programming Language Trends**: JavaScript is the most popular language among these users.

4. **Open Source Engagement**: Many developers don't use a license for their projects. Among those who do, the MIT License is the most common, showing that they are open to sharing their work with few restrictions.

5. **Features for Collaboration**: There is a positive link between using "projects" and "wikis" on repositories. Turning on these features can help get more people involved and make collaboration easier.

6. **Surname Trends**: The most common surnames among developers in London are "Appleton", "Li" etc. suggesting many contributors have English and Asian ethnicity.

7. **Email Sharing Behavior**: Hireable developers are more likely to share their email addresses than those who aren't. Hireable developers are more open to being contacted.

8. **Leader Strength**: Defined as followers divided by `1 + following`. Top users are those with more followers than people they follow, showing they are key figures who provide valuable work.

## An Actionable Recommendation for Developers

- To grow their following, developers should be more active by creating and sharing public repositories. Contributing to more projects shows skills and attracts attention from others.
- Turning on collaboration features like "projects" and "wikis" can boost engagement by making it easier for others to contribute and understand the work.
- Sharing contact details, like an email address, can make a developer more visible to collaborators or employers.
- Developers looking for new opportunities should mark themselves as "hireable" and share their contact information to increase their chances of being approached.
- Companies should encourage developers to be visible on GitHub to build their reputation and support a culture of sharing and learning.
