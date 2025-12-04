import json
from datetime import datetime

def analyze_log(logfile):
    data = {
        "connections": 0,
        "auth_attempts": 0,
        "unique_ips": set()
    }

    with open(logfile, "r") as f:
        for line in f:
            if "[CONNECT]" in line:
                data["connections"] += 1
            if "[AUTH]" in line:
                data["auth_attempts"] += 1
            if "IP=" in line:
                ip = line.split("IP=")[1].split()[0]
                data["unique_ips"].add(ip)

    data["unique_ips"] = list(data["unique_ips"])
    return data

if __name__ == "__main__":
    result = analyze_log("honeypot.log")
    print(json.dumps(result, indent=4))
