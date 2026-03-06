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
- `action` — firewall action: allow / deny / drop
- `bytes` — bytes transferred (integer)

## Completed functions
- `functions/ingest.py` — `ingest(filepath)`: reads CSV, parses timestamp, prints entry count, returns DataFrame
- `functions/filter.py` — `filter_logs(df, **kwargs)`: filters by any column using kwargs, supports single values and lists via `.isin()`, warns on invalid column names

## Up next
- `functions/summary.py` — aggregation and summary stats

## How to help me
- Explain what a pandas method does before I use it
- Suggest which pandas tools fit a given problem
- Ask me questions to guide my thinking
- Only show code snippets if I'm truly stuck and ask for one
- Remind me of relevant pandas docs or methods I might not know yet
- Celebrate progress — this is a learning journey
