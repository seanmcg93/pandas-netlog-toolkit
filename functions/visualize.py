import matplotlib.pyplot as plt
import os
from datetime import datetime
from functions.summary import  traffic_over_time, top_talkers, top_dst_ports


def save_plot(fig, filename, save=False):
    if save:
        project_root = os.path.dirname(os.path.dirname(__file__))
        plots_dir = os.path.join(project_root, "plots")
        os.makedirs(plots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plot = f"{timestamp}_{filename}.png"
        filepath = os.path.join(plots_dir, plot)

        plt.tight_layout()
        fig.savefig(filepath)
        print(f"Plot Generated at:\n"+filepath)
        return filepath
    else:
        plt.tight_layout()
        plt.show()


def plot_traffic_over_time(df, freq='5min', save=False):
    df = traffic_over_time(df, freq)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    df["total_bytes"].plot(ax=ax1)
    df["total_connections"].plot(ax=ax2)
    plot = save_plot(fig, filename="traffic_over_time", save=save)
    return plot


def plot_top_talkers(df, save=False):
    df = top_talkers(df)
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax)
    plt.title("Top Talkers")
    plt.xlabel("src_ips")
    plt.ylabel("total_bytes")
    plt.xticks(rotation=55)
    plot = save_plot(fig, filename="top_talkers", save=save)
    return plot



def plot_top_dst_ports(df, save=False):
    df = top_dst_ports(df)
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax)
    plt.title("Top Destination Ports")
    plt.xlabel("Ports")
    plt.ylabel("Total Connections")
    plt.xticks(rotation=55)
    plot = save_plot(fig, filename="top_dst_ports", save=save)
    return plot





