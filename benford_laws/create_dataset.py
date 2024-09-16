import github_interface
import pandas as pd


def create(username):
    followers_list = github_interface.get_all_followers(username)

    formatted_followers_list = list(
        map(
            lambda x: {
                **x,
                "followers": x["followers"]["totalCount"],
                "following": x["following"]["totalCount"],
            },
            followers_list,
        )
    )

    df = pd.DataFrame(formatted_followers_list)
    df.to_csv(f"./dataset/{username}_followers.csv", index=False)


# create("torvalds")
# create("matz")
