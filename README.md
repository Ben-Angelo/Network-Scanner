# Network Scanner (Terminal-based)

A simple, terminal-based Python tool that discovers devices on a local network, labels them, measures response time, and explains basic network communication concepts in plain English. Designed for learning networking fundamentals, IT support, and entry-level cybersecurity practice.

---

## Features

- Automatically detects the current network (no manual IP input)
- Discovers active devices using ICMP (ping)
- Labels devices as: This PC, Router, or Other Device
- Measures and displays response time (latency)
- Clean, color-coded terminal output
- Cross-platform support (Windows, Linux, Termux)

## How it works (simple)

1. The program detects your device’s local IP address.
2. It determines the network range (a /24 network is used as a fallback).
3. It sends a lightweight ping to each possible host on the network.
4. Devices that respond are marked as alive and timed.

This demonstrates how computers discover and communicate with each other on a local network.

## Requirements

- Python 3.8+
- An active local network connection

Note: This project is written to work with the Python standard library; no external packages are required unless the code in the repository indicates otherwise.

## Tested on

- Windows 10 / 11
- Linux
- Android (Termux)

## Installation

Clone the repository:

```bash
git clone https://github.com/Ben-Angelo/Network-Scanner.git
cd Network-Scanner
```

If this repository contains a requirements.txt file, install dependencies with:

```bash
pip install -r requirements.txt
```

(If there is no requirements.txt, the tool uses the standard library.)

## Usage

Run the scanner from the terminal:

```bash
python host_discovery.py
```

Example output:

```text
Scanning network: 192.168.43.0/24

[+] 192.168.43.1   Router        3 ms
[+] 192.168.43.12  This PC       1 ms
[+] 192.168.43.25  Other Device  7 ms

Scan complete!
Total alive devices: 3
```

## Project structure

```
host_discovery/
│
├── host_discovery.py
├── README.md
└── requirements.txt (optional)
```

## Learning objectives

This project demonstrates foundational concepts including:

- IP addressing and subnet ranges
- ICMP and ping-based host discovery
- Measuring network latency
- Building terminal-based Python tools

## Ethical use notice

This tool is intended for educational purposes only. Only scan networks you own or have explicit permission to test. Unauthorized scanning may be illegal or violate terms of service.

## Future improvements

Suggestions for enhancements:

- Subnet mask detection beyond a /24 fallback
- Device vendor identification (MAC lookup / OUI lookup)
- Optional port scanning (disabled by default)
- Exporting scan results to CSV or JSON

## Author

Benjamin Angelo (Ben-Angelo)

---

