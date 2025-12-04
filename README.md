# **SSH Honeypot**

A lightweight SSH Honeypot designed to capture attacker activity, log credential attempts, and analyze intrusion patterns. Built using Python and Paramiko, this honeypot simulates an SSH service and records connection details for security research and monitoring.

---

## **Features**

* Captures incoming SSH connection attempts
* Logs username and password guesses
* Records attacker IP addresses
* Tracks total connections and failed authentication attempts
* Simple log analysis tool included

---

## **Project Structure**

```
├── ssh_honeypot.py     # Main honeypot server
├── log_analysis.py     # Log analysis script
└── honeypot.log        # Generated logs (after running honeypot)
```

---

## **Requirements**

* Python 3.x
* Paramiko library

```
pip install paramiko
```

---

## **How to Run**

1. Run the honeypot (requires root for port 22):

```
sudo python3 ssh_honeypot.py
```

2. After the honeypot logs activity, analyze logs:

```
python3 log_analysis.py
```

---

## **Output (Example)**

The analysis script returns:

```json
{
    "connections": 12,
    "auth_attempts": 38,
    "unique_ips": ["192.168.1.5", "45.22.19.11"]
}
```

---

## **Disclaimer**

This project is for **educational and research purposes**.
Do not expose the honeypot to the internet unless you understand the risks.

---

If you want, I can make an **advanced GitHub README with badges, images, and architecture diagrams** too.
