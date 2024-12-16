import re


web_server_logs = """
192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020
"""


log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>[A-Z]+)'


matches = re.finditer(log_pattern, web_server_logs)


for match in matches:
    print(f"IP: {match.group('ip')}, Tarix: {match.group('datetime')}, Metod: {match.group('method')}")


import re
import json
web_server_logs = """
192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020
"""
from collections import defaultdict
failed_attempts_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).+ "(?P<method>[A-Z]+).+" 401'
failed_attempts = defaultdict(int)

for match in re.finditer(failed_attempts_pattern, web_server_logs):
    failed_attempts[match.group('ip')] += 1

blocked_ips = {ip: count for ip, count in failed_attempts.items() if count > 5}

with open("blocked_ips.json", "w") as json_file:
    json.dump(blocked_ips, json_file, indent=4)

print("5-dən çox uğursuz giriş edən IP-lər ")
print(blocked_ips)


import re
from collections import defaultdict


web_server_logs = """
192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020
"""

# Uğursuz girişlər üçün regex
failed_attempts_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).+ "(?P<method>[A-Z]+).+" 401'

# IP-lər üzrə uğursuz girişlərin sayı
failed_attempts = defaultdict(int)

for match in re.finditer(failed_attempts_pattern, web_server_logs):
    failed_attempts[match.group('ip')] += 1

# Mətn faylına yazmaq
with open("failed_attempts.txt", "w") as txt_file:
    txt_file.write("IP Address\tFailed Attempts\n")
    txt_file.write("-" * 30 + "\n")
    for ip, count in failed_attempts.items():
        txt_file.write(f"{ip}\t{count}\n")

print("Uğursuz giriş cəhdlərinin siyahısı ")
print(failed_attempts)


import csv
# Regex modeli: IP ünvanı, tarix və HTTP metodunu çıxarmaq
log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>[A-Z]+).+" (?P<status>\d+)'
# Loglardan məlumat çıxarma
log_data = []
for match in re.finditer(log_pattern, web_server_logs):
    log_data.append({
        "ip": match.group("ip"),
        "datetime": match.group("datetime"),
        "method": match.group("method"),
        "status": match.group("status")
    })
with open("web_logs.csv", "w", newline="") as csv_file:      # CSV faylına yazmaq
    fieldnames = ["IP Address", "Date", "HTTP Method", "Failed Attempts"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # Uğursuz girişləri əlavə etmək
    for log in log_data:
        writer.writerow({
            "IP Address": log["ip"],
            "Date": log["datetime"],
            "HTTP Method": log["method"],
            "Failed Attempts": failed_attempts.get(log["ip"], 0)
        })
print("'web_logs.csv' faylı yaradıldı.")