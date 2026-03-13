import matplotlib.pyplot as plt
import os
from datetime import datetime
from functions import traffic_over_time


def plot_traffic_over_time(df, freq='5min', save=False):
    df = traffic_over_time(df, freq)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    df["total_bytes"].plot(ax=ax1)
    df["total_connections"].plot(ax=ax2)

    if save:
        project_root = os.path.dirname(os.path.dirname(__file__))
        plots_dir = os.path.join(project_root, "plots")
        os.makedirs(plots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plot = f"{timestamp}_plot.png"
        filepath = os.path.join(plots_dir, plot)

        fig.savefig(filepath)
        print(f"Plot Generated at:\n"+filepath)
        return filepath
    else:
        plt.show()


