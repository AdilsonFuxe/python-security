import os
import time

count = 0
with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    count = len(dump)
    for ip in dump:
        print("IP/HOST - " + ip)
        os.system("ping -c4 "+ip)
        print("-" * 60)
        time.sleep(3)
print(str(count) + " ips verificados")
