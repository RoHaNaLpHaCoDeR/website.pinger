import time
import requests

websites = [
    "https://wtf-thats-interesting-flask-app.onrender.com/",
    "https://laughter-ka-doze-flask-app.onrender.com/"
]

interval = 600  # 10 minutes

for site in websites:
    try:
        response = requests.get(site)
        print(f"Pinged {site} - Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to ping {site}: {e}")
        print(f"Sleeping for {interval} seconds...\n")
    time.sleep(interval)

print("6 hours completed. Exiting...")
