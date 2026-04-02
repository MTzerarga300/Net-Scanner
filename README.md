# 🛡️ Net-Scanner — Automated Network Scanner & Security Reporter

A Python-based network reconnaissance tool built on Kali Linux.  
Scans a target IP or range and generates a clean HTML security report.

## Features
- Live host discovery
- Open port & service detection
- Service version fingerprinting
- OS detection
- Automatic risk flagging on sensitive ports (22, 80, 443, 3389, etc.)
- Clean dark-themed HTML report output

## Tools & Libraries
- Python 3
- nmap / python-nmap
- Jinja2 (report templating)

## Installation

git clone https://github.com/TTzerarga3000/Net-Scanner.git
cd Net-Scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Usage

sudo python3 main.py

Enter a target IP or range when prompted:
- Single host: 192.168.1.1
- Full range: 192.168.1.0/24

Report is saved to output/report.html

## ⚠️ Legal Notice
This tool is intended for use on your own systems or with explicit permission.  
Unauthorized scanning is illegal.

## Author
ZERARGA Mohamed Tayeb  
4th Year Telecommunications & ICT Engineering — ENSTTIC, Algeria
