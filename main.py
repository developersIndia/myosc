import urllib.parse
import urllib.request
import json, sys, os
import pathlib
from datetime import datetime
from collections.abc import Mapping

HEADERS = {"User-Agent": "Mozilla/5.0"}
DEFAULT_HEADER = """"""
DEFAULT_FOOTER = """"""


def parse_link_header(link_header):
    header_links = link_header.split(",")[0].split(";")
    if header_links[1] == ' rel="next"':
        next_page = header_links[0]
        # yo why tf response headers are not normal ?
        next_page = next_page[1 : len(next_page) - 1]
    else:
        next_page = None

    return next_page


def request(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode("utf-8"))
        if response.headers["link"] is not None:
            next_url = parse_link_header(response.headers["link"])
        else:
            next_url = None

    return res, next_url


def handle_pagination(url):
    res_list = []
    while True:
        res, next_url = request(url)
        if isinstance(res, Mapping):
            # check if response is dict like
            res_list += res["items"]
        else:
            res_list += res
        if next_url is None:
            break
        url = next_url

    return res_list


def get_user_repos(username):
    # eliminate contributions to self repos
    print("Fetching User Repositories ...")
    repos = handle_pagination(
        f"https://api.github.com/users/{username}/repos?type=owner&per_page=100"
    )
    # filter forked repos
    repo_list = [repo["url"] for repo in repos if repo["fork"] is False]

    return repo_list


def get_user_prs(username):
    # get all pull requests of a user
    print(f"Fetching {username}'s Pull Requests ...")
    pull_requests = handle_pagination(
        f"https://api.github.com/search/issues?q=author%3A{username}+type%3Apr&per_page=100"
    )
    return pull_requests


def generate_report(repos, prs):
    header = pathlib.Path("header.md")
    footer = pathlib.Path("footer.md")

    if header.exists():
        with open(f"{user}-pull-requests.md", "w") as file:
            header_file = open("header.md", "r")
            file.write(header_file.read())
            header_file.close()
    else:
        with open(f"{user}-pull-requests.md", "w") as file:
            file.write(DEFAULT_HEADER)


    with open(f"{user}-pull-requests.md", "a+") as file:
        file.write("\n<ol>")
        for pr in prs:
            if pr["repository_url"] not in repos:
                created_date = datetime.strptime(
                    pr["created_at"], "%Y-%m-%dT%H:%M:%SZ"
                ).strftime("%d %b, %Y")
                file.write("\n<li>")
                file.write(
                    f"""<a target="_blank" href="{pr['html_url']}">{pr['title']}</a> in <b><a href="{pr['html_url'][:pr['html_url'].rfind('/pull/')]}">{os.path.basename(pr['repository_url'])}</a></b> on <i>{created_date}</i> \n\n"""
                )
                file.write(f"<details><summary>Description</summary>\n\n")
                file.write(f"{pr['body']}\n</details>\n\n")
                file.write("</li>")
        file.write("</ol>\n\n")

    if footer.exists():
        with open(f"{user}-pull-requests.md", "a+") as file:
            footer_file = open("footer.md", "r")
            file.write(footer_file.read())
            footer_file.close()
    else:
        with open(f"{user}-pull-requests.md", "a+") as file:
            file.write(DEFAULT_FOOTER)


    print(f"Saving context in {user}-pull-requests.md ✅")


if __name__ == "__main__":
    try:
        user = os.environ["INPUT_USERNAME"]
    except KeyError as e:
        print("moc needs a github username")
        exit()
    # if len(sys.argv) != 2:
    #     print("Needs a github username as an argument")
    #     exit()
    # else:
    #     user = sys.argv[1]
    user_repos = get_user_repos(user)
    user_prs = get_user_prs(user)
    generate_report(user_repos, user_prs)
