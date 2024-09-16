import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import common_theme
import numpy as np


def load_dataset(username):
    return pd.read_csv(f"./dataset/{username}_followers.csv")


def get_first_significant_digit(number):
    return int(str(number)[0])


def plot(username, target):
    df = load_dataset(username)
    followers = df[target].to_list()
    not_zero_followers = [f for f in followers if f != 0]

    followers_fsd = list(map(get_first_significant_digit, followers))
    followers_fsd_count = [followers_fsd.count(i) for i in range(1, 10)]

    benford_probs = [np.log10(1 + 1 / i) for i in range(1, 10)]
    benford_preds = [len(not_zero_followers) * prob for prob in benford_probs]

    plot_df = pd.DataFrame(
        {
            "digits": list(range(1, 10)) * 2,
            "Count": followers_fsd_count + benford_preds,
            "Data": ["実データ"] * 9 + ["予測データ"] * 9,
        }
    )

    common_theme.setSettings(xtick_labelbottom=True, ytick_labelleft=True)

    sns.barplot(
        x="digits",
        y="Count",
        hue="Data",
        data=plot_df,
        palette={"実データ": "gray", "予測データ": "limegreen"},
    )

    plt.legend(title="")
    plt.xlabel("一桁目")
    plt.ylabel("出現回数")

    plt.savefig(f"./output/{username}_follower_{target}_plot.png")


# plot("torvalds", "followers")
# plot("matz", "following")
