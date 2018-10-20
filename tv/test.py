import samsungctl
import time

config = {
    "name": "pawel-tv",
    "description": "PC",
    "id": "",
    "host": "192.168.0.25",
    "port": 55000,
    "method": "legacy",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
    print(remote)