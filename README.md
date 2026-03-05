# pandas-netlog-toolkit

A personal learning project for analysing network log CSV files using pandas.

Built as a hands-on learning exercise — each function in the `functions/` folder
is written step by step as new pandas concepts are explored.

## Log format

CSV files with the following fields:

| Field       | Description                          |
|-------------|--------------------------------------|
| timestamp   | Event datetime                       |
| src_ip      | Source IP address                    |
| dst_ip      | Destination IP address               |
| dst_port    | Destination port number              |
| action      | Firewall action (allow/deny/drop)    |
| bytes       | Bytes transferred                    |

## Project structure

```
pandas-netlog-toolkit/
├── functions/          # Individual analysis functions (one concept at a time)
├── sample_data/        # Sample CSV log files for testing
├── requirements.txt    # Python dependencies
├── README.md
└── CLAUDE.md           # Context for AI-assisted learning sessions
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
