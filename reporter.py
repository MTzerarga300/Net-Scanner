from jinja2 import Environment, FileSystemLoader
import os

def generate_report(scan_data):
    """
    Takes scan_data dict from scanner.py
    and generates an HTML report in /output/
    """
    # Load the HTML template
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    # Render the template with scan data
    html_output = template.render(
        target=scan_data["target"],
        scan_time=scan_data["scan_time"],
        hosts=scan_data["hosts"]
    )

    # Save to output folder
    output_path = os.path.join("output", "report.html")
    with open(output_path, "w") as f:
        f.write(html_output)

    print(f"\n[+] Report saved to: {output_path}")
    return output_path
