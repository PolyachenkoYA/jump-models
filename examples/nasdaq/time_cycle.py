import subprocess
import time

subprocess.run(["python", "example.py", "email"])
time_init = 3600 * (1) + 60 * 54
time.sleep(time_init)  # Wait

while(1):
    subprocess.run(["python", "example.py", "email"])
    time_24h = 24*3600
    time.sleep(time_24h)  # Wait



