import os
import csv
import atexit
import dotenv
import requests

dotenv.load_dotenv()

url = "https://api.github.com/graphql"
headers = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
    "Content-Type": "application/json",
}
after = None
query = {}

for i in ["user", "repo"]:
    with open(f"queries/{i}.graphql") as f:
        query[i] = f.read().strip()


def fetch(query, variables):
    response = requests.post(
        url,
        headers=headers,
        json={"query": query, "variables": variables},
    )
    response.raise_for_status()
    return response.json()


def paginate(entity):
    page_info = entity["pageInfo"]
    if page_info["hasNextPage"]:
        return page_info["endCursor"]


users_csv = open("data/users.csv", "w+")
users = csv.writer(users_csv)
users.writerow(
    [
        "login",
        "name",
        "company",
        "location",
        "email",
        "hireable",
        "bio",
        "public_repos",
        "followers",
        "following",
        "created_at",
    ]
)

repos_csv = open("data/repositories.csv", "w")
repos = csv.writer(repos_csv)
repos.writerow(
    [
        "login",
        "full_name",
        "created_at",
        "stargazers_count",
        "watchers_count",
        "language",
        "has_projects",
        "has_wiki",
        "license_name",
    ]
)


@atexit.register
def close_files():
    users_csv.close()
    repos_csv.close()


def write_user(user):
    users.writerow(
        [
            user["login"],
            user["name"],
            user["company"].lstrip("@").upper() if user["company"] else "",
            user["location"],
            user["email"],
            user["isHireable"],
            user["bio"],
            user["repositories"]["totalCount"],
            user["followers"]["totalCount"],
            user["following"]["totalCount"],
            user["createdAt"],
        ]
    )


def write_repo(user, repo):
    repos.writerow(
        [
            user["login"],
            user["login"] + "/" + repo["name"],
            repo["createdAt"],
            repo["stargazerCount"],
            repo["watchers"]["totalCount"],
            repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else "",
            repo["hasProjectsEnabled"],
            repo["hasWikiEnabled"],
            repo["licenseInfo"]["key"] if repo["licenseInfo"] else "",
        ]
    )


while True:
    data = fetch(query["user"], {"after": after})
    entity = data["data"]["search"]

    # Even though the search query is for users,
    # api may return other enitites as empty {}. Skip them.
    filtered = filter(None, entity["nodes"])

    for user in filtered:
        write_user(user)

    if not (after := paginate(entity)):
        break

users_csv.seek(0)

for user in csv.DictReader(users_csv):
    count = 0

    while count < 500:
        data = fetch(query["repo"], {"login": user["login"], "after": after})
        entity = data["data"]["user"]["repositories"]

        limited = entity["nodes"][: 500 - count]
        count += len(limited)

        for repo in limited:
            write_repo(user, repo)

        if not (after := paginate(entity)):
            break
