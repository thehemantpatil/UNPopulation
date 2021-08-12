import matplotlib.pyplot as mt
import india_plot
import saarc
import grouped_plot
import south_asia


def plotting():
    """
     - import all the files and plot it.
    """
    india_plot.indiapopulation()
    south_asia.south()
    saarc.saarc()
    grouped_plot.grouped()

    mt.tight_layout()
    mt.show()
