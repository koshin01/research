import requests
from dotenv import load_dotenv
import os
import sys


def load_request_headers():
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    return {
        "Authorization": f"Bearer {token}",
    }


def get_all_followers(username):
    query = """
        query($username: String!, $afterCursor: String) {
            user(login: $username) {
                followers(first: 100, after: $afterCursor) {
                    edges {
                        node {
                            followers {
                                totalCount
                            }
                            following {
                                totalCount
                            }
                        }
                    }
                    pageInfo {
                        endCursor
                        hasNextPage
                    }
                }
            }
        }
    """
    headers = load_request_headers()

    sys.setrecursionlimit(3000)

    def fetch_followers(end_cursor=None):
        variables = {
            "username": username,
            "afterCursor": end_cursor,
        }
        response = requests.post(
            "https://api.github.com/graphql",
            json={"query": query, "variables": variables},
            headers=headers,
        )
        response.raise_for_status()
        print(response.headers.get("X-RateLimit-Remaining"))

        data = response.json()["data"]
        followers_batch = data["user"]["followers"]["edges"]
        page_info = data["user"]["followers"]["pageInfo"]

        yield from (follower["node"] for follower in followers_batch)

        if page_info["hasNextPage"]:
            yield from fetch_followers(page_info["endCursor"])

    return list(fetch_followers())
