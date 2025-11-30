# Firewall Security – Advanced Packet Filtering & Threat Detection

![Build Status](https://img.shields.io/badge/build-stable-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Firewall Security is an advanced packet filtering, monitoring, and threat detection system designed for cybersecurity studies, SOC training, and network traffic analysis.

## Project Structure
```
📁 README.md
📁 firewall.py
📁 monitor.py
📁 scanner.py
📁 utils.py
📂 configs/
   ├── rules.json
   ├── whitelist.txt
   └── blacklist.txt
📂 logs/
   └── firewall.log
```

## rules.json Example
```json
{
    "block_ports": [23, 445],
    "allow_ports": [80, 443],
    "alert_ports": [21],
    "dos_threshold": 40
}
```

## Demonstrations

### Firewall Simulation
```
[BLOCK] 192.168.1.16 → rule-matched
[ALLOW] 192.168.1.15 → whitelist
[ALLOW] 192.168.1.19 → random-check OK
```

### DoS Detection
```
THRESHOLD: 40 pkts/s
Monitoring traffic…
⚠️ BLOCKED 192.168.2.19 (40.32 pkts/s)
```

## Features
- ⚡ Real-time packet monitoring  
- 🔥 Automatic rule-based blocking  
- 🚨 DoS detection via threshold  
- 🛑 Whitelist & blacklist support  
- 📝 Log generation + rotation  
- 🧪 Simulation mode (no sudo)

## Challenges Faced
- Root sniffer → simulation mode added  
- High packet volume → lightweight loop  
- DoS threshold tuning → JSON-based  
- Port conflicts → auto-detected early  
- Log growth → manual rotation system  

## Installation
```bash
git clone https://github.com/LeoPanarella/FireWall-Python.git
cd FireWall-Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
sudo python3 firewall.py
python3 monitor.py --simulate
```

## Author
Developed by Leonardo Panarella

## License
MIT License
