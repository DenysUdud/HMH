import calendar
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt


def plot_calendar(days, months):
    """
    A function builds calendar with pointed dates.
    e.g
    plot_calendar([2,3,4,5,6,9], [7,7,7,7,7,9]).
    There will be build calendar with such pointed days: 02.07-06.07
    and 09.09 (dd.mm)

    :param days: list: list with days of months, which will be
                        pointed.
    :param months: list: list with number of months in which days
                        will be pointed.
    :return: None
    """
    plt.figure(figsize=(9, 3))
    # non days are grayed
    ax = plt.gca().axes
    ax.add_patch(Rectangle((29, 2), width=.8, height=.8,
                           color='gray', alpha=.3))
    ax.add_patch(Rectangle((30, 2), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 2), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 4), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 6), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 9), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 11), width=.8, height=.8,
                           color='gray', alpha=.5))
    for d, m in zip(days, months):
        ax.add_patch(Rectangle((d, m),
                               width=.8, height=.8, color='C0'))
    plt.yticks(np.arange(1, 13)+.5, list(calendar.month_abbr)[1:])
    plt.xticks(np.arange(1,32)+.5, np.arange(1,32))
    plt.xlim(1, 32)
    plt.ylim(1, 13)
    plt.gca().invert_yaxis()
    # remove borders and ticks
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.tick_params(top=False, bottom=False, left=False, right=False)
    plt.show()