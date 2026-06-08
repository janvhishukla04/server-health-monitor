import psutil
import datetime
import time

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

def check_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_alerts(cpu, memory, disk):
    alerts = []
    if cpu > 80:
        alerts.append(f"ALERT: High CPU usage - {cpu}%")
    if memory > 80:
        alerts.append(f"ALERT: High Memory usage - {memory}%")
    if disk > 90:
        alerts.append(f"ALERT: High Disk usage - {disk}%")
    return alerts

def generate_report():
    now = datetime.datetime.now()
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    alerts = check_alerts(cpu, memory, disk)

    report = f"""
============================
Server Health Report
============================
Time     : {now}
CPU      : {cpu}%
Memory   : {memory}%
Disk     : {disk}%
============================
"""
    if alerts:
        report += "\n[WARNING] ALERTS:\n"
        for alert in alerts:
            report += f"  -> {alert}\n"
    else:
        report += "\n[OK] All systems normal\n"

    print(report)

    with open("health_log.txt", "a") as f:
        f.write(report)

# Auto repeat every 10 seconds
while True:
    generate_report()
    time.sleep(10)