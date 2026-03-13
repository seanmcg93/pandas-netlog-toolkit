from datetime import datetime
import os

from functions import action_count, top_talkers, top_dst_ports, flag_high_traffic, cross_reference, traffic_over_time


def generate_report(df):
    project_root = os.path.dirname(os.path.dirname(__file__))
    reports_dir = os.path.join(project_root, "reports")
    os.makedirs(reports_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report = f"{timestamp}_Report.txt"
    count = action_count(df).to_string()
    talkers = top_talkers(df).to_string()
    ports = top_dst_ports(df).to_string()
    flagged = flag_high_traffic(df).to_string()
    flagged_high_droprate = cross_reference(df).to_string()
    traffic_time = traffic_over_time(df).to_string()
    filepath = os.path.join(reports_dir, report)

    lines = ["Number of Allowed and Blocked Packets:\n"+count+"\n",
             "========================================================\n",
             "Top 10 Source IP and transfer bytes:\n"+talkers+"\n",
             "========================================================\n",
             "Top 10 Most Used Ports:\n"+ports+"\n",
             "========================================================\n",
             "Flagged Source IPs:\n"+flagged+"\n",
             "========================================================\n",
             "Flagged with Drop Rate over 20%:\n"+flagged_high_droprate+"\n",
             "========================================================\n",
             "Traffic over Time:\n"+traffic_time+"\n",
             "========================================================\n"]

    with open(filepath, "w") as file:
       file.writelines(lines)
    print(f"Report Generated at:\n"+filepath)
    return filepath



