import subprocess
import time

while(1):
    subprocess.run(["python", "example.py", "email"])
    time_24h = 24*3600
    time.sleep(time_24h)  # Wait



