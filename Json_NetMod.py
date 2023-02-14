import json
import socket
with open('config.json') as f:
    config = json.load(f)
config
output = json.dumps(config)
output
