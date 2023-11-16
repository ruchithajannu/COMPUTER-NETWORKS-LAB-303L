#AP21110010140
import subprocess

# Define the target host or IP address you want to ping
host = "google.com"

# Run the ping command and capture its output
try:
    result = subprocess.check_output(['ping', '-4',host], universal_newlines=True)
    print(result)
except subprocess.CalledProcessError as e:
    print("Ping failed with error code", e.returncode)