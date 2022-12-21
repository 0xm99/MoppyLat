import time
import json
from web3 import Web3

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

with open("settings.json") as f:
    settings = json.load(f)

endpoints = settings["endpoints"]

request_times = {}
print ("")
print ("Moppy Node Python Latency tester")
print ("v0.1")
print ("")
print(colored(255, 0, 0,"moppynodes.com"))

for endpoint in endpoints:
    request_times[endpoint] = []
    if endpoint.startswith("http"):
        web3 = Web3(Web3.HTTPProvider(endpoint))
    elif endpoint.startswith("ws"):
        web3 = Web3(Web3.WebsocketProvider(endpoint))
    else:
        print(f"Unsupported endpoint: {endpoint}")
        continue
    request_count = 0
    while request_count < 1000:
        start_time = time.time()
        code = web3.eth.get_code("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56")
        end_time = time.time()
        request_times[endpoint].append(end_time - start_time)
        request_count += 1
        print(f"request n° {request_count} - endpoint {endpoint}: {'{:.3f}'.format((end_time - start_time) * 1000)} millisecondes.", end="\r")
        

for endpoint, times in request_times.items():
    average_time = sum(times) / len(times)
    
    print(f"Average latency time for {endpoint} is  {'{:.3f}'.format(average_time * 1000)} millisecondes.")

print(colored(255, 0, 0,"moppynodes.com"))
