import matplotlib
import seaborn as sns

rc = {
    "figure.figsize": [10, 5],
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "font.family": "Helvetica Neue",
    'font.style': 'normal',
    "font.size": 18,
    "axes.labelsize": 18,
    "axes.titlesize": 18,
    "xtick.labelsize": 15,
    "ytick.labelsize": 15,
    "legend.fontsize": 15,

    # lines
    "axes.linewidth": 1.25,
    "lines.linewidth": 1.75,
    "patch.linewidth": 1,

    # grid
    # "axes.grid": True,
    "axes.grid.axis": 'x',
    "axes.grid.which": "major",
    "grid.linestyle": "--",
    "grid.linewidth": 0.75,
    "grid.alpha": 0.75,

    # ticks
    # "xtick.top": True,
    # "ytick.right": True,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.minor.visible": False,
    "ytick.minor.visible": False,
    "xtick.major.width": 1.25,
    "ytick.major.width": 1.25,
    "xtick.minor.width": 1,
    "ytick.minor.width": 1,
    "xtick.major.size": 7,
    "ytick.major.size": 7,
    "xtick.minor.size": 5,
    "ytick.minor.size": 5,

    'lines.markeredgewidth': 0,  # 1.5,
    "lines.markersize": 5,
    "lines.markeredgecolor": "k",
    'axes.titlelocation': 'center',
    "axes.formatter.limits": [-3, 3],
    "axes.formatter.use_mathtext": True,
    "axes.formatter.min_exponent": 2,
    'axes.formatter.useoffset': False,
    "figure.autolayout": False,
    "hist.bins": "auto",
    "scatter.edgecolors": "k"
}


def set_mpl(palette='shap', desat=0.8):
    sns.set_context('notebook', font_scale=1.25)
    matplotlib.rcParams.update(rc)
    if palette == 'shap':
        # colors from shap package: https://github.com/slundberg/shap
        cp = sns.color_palette(
            ["#1E88E5", "#ff0d57", "#13B755", "#7C52FF", "#FFC000", "#00AEEF"]
            )
        sns.set_palette(cp, color_codes=True, desat=desat)
    elif palette == 'shap_paired':
        # colors from shap package: https://github.com/slundberg/shap
        # + SB pairing of colors
        cp = sns.color_palette([
            "#1E88E5", "#1e25e5", "#ff0d57", "#ff5a8c", "#13B755",
            "#2de979", "#7C52FF", "#b69fff", "#FFC000", "#ffd34d",
            "#00AEEF", '#3dcaff'
        ])
        sns.set_palette(cp, color_codes=True, desat=desat)
    else:
        sns.set_palette(palette, color_codes=True, desat=desat)

    # Turn off the upper and right spines
    matplotlib.rcParams['axes.spines.top'] = False
    matplotlib.rcParams['axes.spines.right'] = False


set_mpl()