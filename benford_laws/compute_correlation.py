import pandas as pd
import numpy as np


def load_dataset(username):
    return pd.read_csv(f"./dataset/{username}_followers.csv")


def get_first_significant_digit(number):
    return int(str(number)[0])


def compute(username, target):
    df = load_dataset(username)
    followers = df[target].to_list()
    print(len(followers))

    followers_fsd = list(map(get_first_significant_digit, followers))
    followers_fsd_count = [followers_fsd.count(i) for i in range(1, 10)]

    benford_probs = [np.log10(1 + 1 / i) for i in range(1, 10)]

    correlation_matrix = np.corrcoef(followers_fsd_count, benford_probs)
    print(correlation_matrix)


# compute("torvalds", "followers")
# compute("matz", "following")
