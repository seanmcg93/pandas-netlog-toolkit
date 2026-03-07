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



