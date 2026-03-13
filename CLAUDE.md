# CLAUDE.md — Context for AI-assisted learning sessions

## About me
- I am still learning Python — guide and hint, do not write code for me
- I am a network analyst learning pandas for log analysis
- Teaching style: explain concepts, suggest ideas, let me implement

## Current skill level
- Comfortable with list comprehensions, f-strings, basic pandas filtering
- Familiar with groupby and value_counts
- Building deeper pandas knowledge through this project

## Log data format
CSV network logs with the following fields:
- `timestamp` — event datetime (string, needs parsing)
- `src_ip` — source IP address
- `dst_ip` — destination IP address
- `dst_port` — destination port number (integer)
- `action` — firewall action: allow / block
- `bytes` — bytes transferred (integer)

## Completed functions
- `functions/ingest.py` — `ingest(filepath)`: reads CSV, parses timestamp, prints entry count, returns DataFrame
- `functions/filter.py` — `filter_logs(df, **kwargs)`: filters by any column using kwargs, supports single values and lists via `.isin()`, warns on invalid column names
- `functions/summary.py` — aggregation and summary stats:
  - `action_count(df)`: returns value counts of firewall actions (allow/block)
  - `top_talkers(df, n=10)`: returns top N src_ips by total bytes transferred
  - `top_dst_ports(df, n=10)`: returns top N destination ports by connection count
  - `flag_high_traffic(df, threshold=2)`: flags src_ips with bytes > mean + (threshold * std) — statistical anomaly detection
  - `traffic_over_time(df, freq='5min')`: resamples traffic into time buckets, returns total_bytes and total_connections per window — useful for spotting spikes during IR
  - `cross_reference(df, traffic_threshold=2, deny_threshold=0.2)`: flags src_ips with both high traffic volume AND high block rate — stronger anomaly signal for IR
- `functions/report.py` — `generate_report(df)`: calls all summary functions including `traffic_over_time` and `cross_reference`, writes a timestamped `.txt` report to `reports/`, returns filepath
- `functions/visualize.py` — plotting functions using `matplotlib`:
  - `plot_traffic_over_time(df, freq='5min', save=False)`: dual subplot line chart of total_bytes and total_connections over time, optionally saves to `plots/`

## Up next
- Add bar chart functions to `functions/visualize.py`
  - Bar chart for `top_talkers` (top src_ips by bytes)
  - Bar chart for `top_dst_ports` (top ports by connection count)

## How to help me
- Explain what a pandas method does before I use it
- Suggest which pandas tools fit a given problem
- Ask me questions to guide my thinking
- Only show code snippets if I'm truly stuck and ask for one
- Remind me of relevant pandas docs or methods I might not know yet
- Celebrate progress — this is a learning journey
