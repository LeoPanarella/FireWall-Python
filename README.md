📘 Firewall Security — Advanced Packet Filtering & Network Threat Detection System

Firewall Security is a modular, extensible, and research-focused project designed for advanced learning and practical experimentation in cybersecurity, network traffic analysis, and threat detection.

This system simulates real firewall behavior, including:

packet inspection,

dynamic rule enforcement,

access control lists,

anomaly detection,

automated threat response.

Ideal for professionals, advanced students, and analysts who want hands-on experience with defensive security mechanisms used in real infrastructures.

🚀 Key Features

Intelligent packet filtering
Custom rules to allow, block, or alert based on ports, IPs, and behavioral triggers.

DoS & anomaly detection
Real-time packet rate analysis with automatic blocking when thresholds are reached.

Integrated packet sniffer (optional)
Real traffic capture and analysis using Scapy.

Professional whitelist / blacklist system
Granular access control for trusted and untrusted sources.

Structured logging system
Essential for auditing and forensic analysis.

Modular architecture
Fully extensible for custom security modules.

📂 Project Structure
Firewall-Security/
│
├── README.md
├── firewall.py
├── monitor.py
├── scanner.py
├── utils.py
│
├── configs/
│   ├── rules.json
│   ├── whitelist.txt
│   └── blacklist.txt
│
└── logs/
    └── firewall.log

🧪 Demonstrations
📝 Log example
[Firewall] Blocking Nimda — Source IP: 192.168.2.36

🚨 DoS attack detection & mitigation

Firewall analysis:

THRESHOLD = 40
Monitoring network traffic...

Blocking IP: 192.168.2.19 | packet rate: 40.32 pkts/s


Attacker generating packets:

Sent 1 packet.
Sent 1 packet.
Sent 1 packet.
...

🔥 Firewall simulation
IP: 192.168.1.16  | Action: BLOCK | Reason: rule-matched
IP: 192.168.1.15  | Action: ALLOW | Reason: whitelist
IP: 192.168.1.19  | Action: ALLOW | Random check: OK

🛠️ Installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install scapy   # optional

▶️ Execution
python3 firewall.py
python3 monitor.py
sudo python3 monitor.py  # for sniffing mode

⚙️ Rule Configuration

Example rules.json:

{
  "block_ports": [23, 445],
  "allow_ports": [80, 443],
  "alert_ports": [21]
}

⚠️ Notice

This project is for educational purposes only.
Network analysis should only be performed on authorized environments.

👤 Author

Leonardo Panarella Neto
GitHub: https://github.com/LeoPanarella
