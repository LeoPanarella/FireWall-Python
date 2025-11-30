from typing import Dict


class FirewallSimulator:
    def __init__(self, rules: Dict[str, str] = None):
        self.rules = rules or {}

    def check(self, ip: str) -> str:
        return self.rules.get(ip, 'allow')

    def add_rule(self, ip: str, action: str):
        self.rules[ip] = action

    def remove_rule(self, ip: str):
        self.rules.pop(ip, None)


def generate_random_ip(seed: int = None):
    import random
    if seed is not None:
        random.seed(seed)
    return f"192.168.1.{random.randint(0, 250)}"


if __name__ == '__main__':
    f = FirewallSimulator({
        '192.168.1.1': 'block',
        '192.168.1.4': 'block',
    })
    for _ in range(10):
        ip = generate_random_ip()
        print(ip, f.check(ip))