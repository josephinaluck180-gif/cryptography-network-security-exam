# Firewall Rules and Verification Log

### Applied Firewall Configuration (iptables)
```bash
# 1. Block guest network completely from the student records server
sudo iptables -A INPUT -s 192.168.20.0/24 -d 192.168.1.100 -j DROP

# 2. Permit authorized staff network access to the Service (Port 5432)
sudo iptables -A INPUT -p tcp -s 192.168.10.0/24 -d 192.168.1.100 --dport 5432 -j ACCEPT

# 3. Block other inbound access to that specific service
sudo iptables -A INPUT -p tcp --dport 5432 -j DROP
```

### Verification Matrix

| Test Case | Command Run | Expected Outcome | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **1. Permitted Connection** (From Staff IP `192.168.10.15`) | `nc -zv 192.168.1.100 5432` | Connection Succeeded | Connection open / succeeded | **PASSED** |
| **2. Blocked Connection** (From Guest IP `192.168.20.50`) | `nc -zv 192.168.1.100 5432` | Connection Timed Out / Dropped | Connection timed out | **PASSED** |
| **3. Blocked External** (From Rogue External `198.51.100.4`) | `nc -zv 192.168.1.100 5432` | Connection Refused / Dropped | Connection timed out | **PASSED** |
