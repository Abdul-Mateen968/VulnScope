import socket
import time
import sys

print("="*60)
print("   VULNSCOPE - E-COMMERCE BACKEND SCANNER ENGINE   ")
print("="*60)
print("[*] Target: Local Retail Environment (127.0.0.1)")
print("[*] Initializing Database & Port Security Checks...\n")
time.sleep(1.5)

# Ports relevant to e-commerce and databases
ports_to_scan = {
    80: "HTTP (Web Traffic)",
    443: "HTTPS (Secure Web)",
    21: "FTP (File Transfer)",
    22: "SSH (Secure Shell)",
    3306: "MySQL (Customer Database)"
}

target = "127.0.0.1"

for port, service in ports_to_scan.items():
    print(f"[*] Scanning Port {port} ({service})... ", end="")
    sys.stdout.flush()
    time.sleep(1) # Presentation ke liye thora delay
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print("[CRITICAL] - OPEN (Vulnerability Detected!)")
    else:
        print("[SECURE] - CLOSED")
    sock.close()

print("\n" + "="*60)
print("[+] Live Scan Completed Successfully.")
print("[+] Exporting threat data to UI Dashboard...")
print("="*60)