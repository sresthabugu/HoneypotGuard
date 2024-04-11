HoneypotGuard

This project implements a basic honeypot named HoneypotGuard to detect and analyze suspicious activity on a network. It leverages Python libraries for packet capture and analysis, integrates with Snort for real-time threat detection, and sends captured data to the ELK Stack for further investigation and visualization.

Requirements

Python (version 3.x recommended)
pip (Python package manager)
Wireshark (network packet analyzer)
Snort (intrusion detection system)
ELK Stack (Elasticsearch, Logstash, Kibana)
Installation

System Setup:

Ensure you have the required software installed (refer to the Requirements section).
Create a dedicated user account for running HoneypotGuard for enhanced security.
Project Structure:

Clone or download this repository.
The project directory should have the following subdirectories:
python: Contains Python code for core functionalities.
config: Stores configuration files (if needed).
logs: Stores logs generated during operation.
data: Stores captured network data (optional).

Python Dependencies:
Activate a virtual environment (recommended) to isolate project dependencies. You can use tools like venv or virtualenv.
Install required Python libraries using pip:
pip install scapy pyshark python-elk-client snortlib

Wireshark Configuration:
Open Wireshark and select the network interface you want to use for capturing traffic destined for the honeypot.
Snort Configuration:

Configure Snort rules to detect specific threats relevant to your honeypot deployment.
Ensure Snort is configured to log alerts in a format compatible with your ELK Stack setup.
ELK Stack Configuration:

Install and configure Elasticsearch, Logstash, and Kibana according to the official documentation for your operating system.
Create an index in Elasticsearch named "honeypot_guard" to store captured packet data.
Define pipelines in Logstash to process and enrich captured data for better analysis.
Design visualizations in Kibana to monitor and investigate suspicious activity.

Run HoneypotGuard:

Navigate to the project directory in your terminal.
Activate the virtual environment (if used).
Run the honeypot.py script:
Bash
python python/honeypot.py


We welcome contributions to this project! Feel free to create pull requests with improvements or additional features.
