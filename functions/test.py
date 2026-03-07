from functions import ingest, action_count, filter_logs, top_talkers, top_dst_ports, flag_high_traffic

rf = ingest("/home/macg/projects/pandas-netlog-toolkit/sample_data/network_logs.csv")

print(flag_high_traffic(rf))



