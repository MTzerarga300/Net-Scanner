from scanner import scan_network
from reporter import generate_report

print("=" * 40)
print("   NET-SCANNER by ZERARGA Mohamed Tayeb")
print("=" * 40)

target = input("\nEnter target IP or range (e.g. 192.168.1.1 or 192.168.1.0/24): ")

# Run scan
scan_data = scan_network(target)

# Generate report
generate_report(scan_data)

print("\n[✓] Done. Open output/report.html in your browser to view the report.")
