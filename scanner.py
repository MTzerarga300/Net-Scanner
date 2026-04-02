import nmap
import datetime

def scan_network(target):
    """
    Scans the target IP or range.
    target can be: '192.168.1.1' or '192.168.1.0/24'
    """
    scanner = nmap.PortScanner()

    print(f"\n[*] Starting scan on: {target}")
    print("[*] This may take a moment...\n")

    # -sV = service version detection
    # -O  = OS detection
    # -T4 = faster scan timing
    scanner.scan(hosts=target, arguments='-sV -O -T4 --open')

    results = {
        "target": target,
        "scan_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hosts": []
    }

    # Sensitive ports that should raise a flag
    risky_ports = [21, 23, 80, 443, 3389, 8080, 445, 139, 22]

    for host in scanner.all_hosts():
        host_data = {
            "ip": host,
            "status": scanner[host].state(),
            "os": "Unknown",
            "ports": []
        }

        # Try to get OS info
        if "osmatch" in scanner[host] and scanner[host]["osmatch"]:
            host_data["os"] = scanner[host]["osmatch"][0]["name"]

        # Loop through open ports
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                port_data = {
                    "port": port,
                    "protocol": proto,
                    "state": service["state"],
                    "service": service["name"],
                    "version": service["version"],
                    "risk": "⚠️ SENSITIVE" if port in risky_ports else "OK"
                }
                host_data["ports"].append(port_data)

        results["hosts"].append(host_data)

    print(f"[+] Scan complete. Found {len(results['hosts'])} host(s).")
    return results


# Quick test — run scanner.py directly to see raw output
if __name__ == "__main__":
    target = input("Enter target IP or range (e.g. 192.168.1.0/24): ")
    data = scan_network(target)

    for host in data["hosts"]:
        print(f"\nHost: {host['ip']} | Status: {host['status']} | OS: {host['os']}")
        for p in host["ports"]:
            print(f"  Port {p['port']}/{p['protocol']} - {p['service']} {p['version']} [{p['risk']}]")
