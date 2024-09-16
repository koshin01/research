import seaborn as sns
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


def setSettings(xtick_labelbottom: bool = False, ytick_labelleft: bool = False):
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
    font_prop = fm.FontProperties(fname=font_path)

    custom_params = {
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.edgecolor": "grey",
        "xtick.labelbottom": xtick_labelbottom,
        "ytick.labelleft": ytick_labelleft,
        "font.family": font_prop.get_name(),
        "lines.linewidth": 3,
    }
    sns.set_theme(style="white", rc=custom_params)

    plt.figure(figsize=(10, 6), dpi=300)


def formattVerticalWritting(text: str):
    return "\n".join(text)
