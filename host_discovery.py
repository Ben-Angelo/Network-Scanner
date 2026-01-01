# It automatically detects my local network, 
# performs ICMP-based host discovery, explains results
#  in plain English, and measures network responsiveness.


import subprocess
import socket
import time
import platform

# ---------- NETWORK HELPERS ----------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_base_ip(ip):
    return ".".join(ip.split(".")[:3])

def get_gateway_ip(base_ip):
    return f"{base_ip}.1"

# ---------- PING FUNCTION ----------
def ping_host(ip):
    system = platform.system()
    start = time.time()

    if system == "Windows":
        cmd = ["ping", "-n", "1", "-w", "1000", ip]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    end = time.time()
    response_time = round((end - start) * 1000, 2)

    if result.returncode == 0:
        return True, response_time
    return False, None

# ---------- TERMINAL COLORS ----------
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ---------- SCANNER ----------
def scan_network(base_ip, local_ip):
    gateway_ip = get_gateway_ip(base_ip)
    alive_hosts = []

    print(f"\nScanning network: {base_ip}.0/24\n")
    print("Legend:")
    print(" - This PC → your device")
    print(" - Router → network gateway")
    print(" - Other → another device\n")

    start_time = time.time()

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        alive, rtt = ping_host(ip)
        if alive:
            if ip == local_ip:
                label = "This PC"
                color = CYAN
            elif ip == gateway_ip:
                label = "Router"
                color = YELLOW
            else:
                label = "Other device"
                color = GREEN
            alive_hosts.append(ip)
            print(f"{color}[+] {ip:<15} | {label:<12} | Response time: {rtt} ms{RESET}")

    duration = round(time.time() - start_time, 2)
    print("\nScan complete!")
    print(f"Total alive devices: {len(alive_hosts)}")
    print(f"Scan duration: {duration} seconds")

# ---------- MAIN ----------
if __name__ == "__main__":
    local_ip = get_local_ip()
    base_ip = get_base_ip(local_ip)
    print(f"Your IP address: {local_ip}")
    scan_network(base_ip, local_ip)
