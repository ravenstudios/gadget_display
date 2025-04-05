import subprocess

def scan_wifi():
    result = subprocess.run(["sudo", "iwlist", "wlan0", "scan"], capture_output=True, text=True)
    ssids = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("ESSID:"):
            ssid = line.split(":")[1].strip().strip('"')
            if ssid:
                ssids.append(ssid)
    return ssids
