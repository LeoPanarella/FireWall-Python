import os
import time
from collections import defaultdict
from pathlib import Path
try:
    from scapy.all import sniff, IP
except Exception:
    sniff = None
    IP = None

CONFIG_DIR = Path(__file__).resolve().parents[1] / 'configs'
WHITELIST_FILE = CONFIG_DIR / 'whitelist.txt'
BLACKLIST_FILE = CONFIG_DIR / 'blacklist.txt'

THRESHOLD = 40

def read_ip_list(path):
    if not path.exists():
        return set()
    with open(path) as f:
        return {line.strip() for line in f if line.strip() and not line.startswith('#')}

def log_event(msg):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"[{t}] {msg}")

def packet_callback_factory(packet_count, blocked_ips, start_time, whitelist, blacklist, dry_run=True):
    def packet_callback(packet):
        if IP is None:
            return
        if not packet.haslayer(IP):
            return
        src_ip = packet[IP].src
        if src_ip in whitelist:
            return
        if src_ip in blacklist and src_ip not in blocked_ips:
            log_event(f"Blacklisted IP seen: {src_ip} -> enforcing block")
            if not dry_run:
                os.system(f"iptables -A INPUT -s {src_ip} -j DROP")
            blocked_ips.add(src_ip)
            return
        packet_count[src_ip] += 1
        current_time = time.time()
        interval = current_time - start_time[0]
        if interval >= 1:
            for ip, count in list(packet_count.items()):
                rate = count / interval
                if rate > THRESHOLD and ip not in blocked_ips:
                    log_event(f"Threshold exceeded: {ip} rate={rate:.1f}")
                    if not dry_run:
                        os.system(f"iptables -A INPUT -s {ip} -j DROP")
                    blocked_ips.add(ip)
            packet_count.clear()
            start_time[0] = current_time
    return packet_callback

def main(dry_run=True):
    whitelist = read_ip_list(WHITELIST_FILE)
    blacklist = read_ip_list(BLACKLIST_FILE)
    packet_count = defaultdict(int)
    blocked_ips = set()
    start_time = [time.time()]
    cb = packet_callback_factory(packet_count, blocked_ips, start_time, whitelist, blacklist, dry_run=dry_run)
    print('Monitor started. Dry-run =', dry_run)
    if sniff is None:
        print('Scapy not available. Exiting.')
        return
    sniff(filter='ip', prn=cb)

if __name__ == '__main__':
    main(dry_run=True)