import numpy as np


def action_count(df):
    count = df["action"].value_counts()
    return count


def top_talkers(df, n=10):
    talks_alot = df.groupby("src_ip")["bytes"].sum().sort_values(ascending=False).head(n)
    return talks_alot


def top_dst_ports(df, n=10):
    port_connections = df.groupby("dst_port").size().sort_values(ascending=False).head(n)
    return port_connections


def flag_high_traffic(df, threshold=2):
    ip_total_bytes = df.groupby("src_ip")["bytes"].sum()
    average = ip_total_bytes.mean()
    deviation = ip_total_bytes.std()
    base_line = average + threshold * deviation
    flagged = ip_total_bytes[ip_total_bytes >= base_line]
    return flagged


def cross_reference(df, traffic_threshold=2, deny_threshold=0.2):
    flagged_ips = flag_high_traffic(df)
    df = df[df["src_ip"].isin(flagged_ips.index)]
    total_connections = df.groupby("src_ip")["action"].count()
    total_blocks = df[df["action"]=="block"].groupby("src_ip")["action"].count()
    drop_rate = total_blocks / total_connections
    df = drop_rate[drop_rate >= deny_threshold]
    return df


def traffic_over_time(df, freq="5min"):
    resample = df.set_index("timestamp").resample(freq).agg({"bytes":"sum", "action": "count"}).rename(columns={"bytes":"total_bytes","action":"total_connections"})
    return resample




