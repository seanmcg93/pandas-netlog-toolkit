# CLAUDE.md — Project context

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
  - `detect_beaconing(df, min_connections=5, interval_std_threshold=5.0)`: flags src_ip/dst_ip pairs with suspiciously regular connection intervals — C2 beacon detection
  - `detect_port_scan(df, freq='1min', port_hits=10)`: flags src_ips hitting many distinct dst_ports within a time window — recon detection
- `functions/report.py` — `generate_report(df, freq='5min')`: calls all summary and plot functions, writes a timestamped `.txt` report to `reports/` with embedded plot filepaths, returns filepath
- `functions/visualize.py` — plotting functions using `matplotlib`:
  - `plot_traffic_over_time(df, freq='5min', save=False)`: dual subplot line chart of total_bytes and total_connections over time, optionally saves to `plots/`
  - `plot_top_talkers(df, save=False)`: bar chart of top src_ips by total bytes, optionally saves to `plots/`
  - `plot_top_dst_ports(df, save=False)`: bar chart of top destination ports by connection count, optionally saves to `plots/`

## Tool purpose
Primary use case is **Incident Response (IR)** — built for triage under time pressure, not general log analysis. Prioritize speed and signal quality.

## Up next (IR-priority order)
1. **Pre-CLI polish** — fix these issues before building the CLI:
   - `detect_beaconing` mutates the passed-in df (line 46 adds `time_delta` column) — fix with `.copy()`
   - `ingest.py` — sort by timestamp on load so beaconing/port scan functions work correctly on unsorted data
   - `visualize.py` — repeated save/path logic in all three plot functions — extract a small helper to remove duplication
   - `filter.py` — replace `type(value) != list` with `isinstance(value, list)` (more Pythonic)
2. **CLI interface** — `argparse`-based `main.py` so the toolkit can be run from terminal (e.g. `python main.py --report --freq 1h`) — critical for IR so analysts aren't dropping into a REPL under pressure; integrate `rich` for colored terminal output, formatted tables, and highlighted anomalies (e.g. red for beaconing, yellow for high traffic)
3. `geo_lookup(df)` in `functions/summary.py` — enrich src/dst IPs with country data using a library like `geoip2` — useful for reporting, not urgent for triage

## Future improvements
- **Time range filtering** — add `filter_by_timerange(df, start, end)` to `functions/filter.py`
- **Data quality** — handle malformed rows in `ingest.py` (missing `bytes`, bad timestamps, etc.) — important for IR where logs may come from multiple messy sources

