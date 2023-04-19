import os

# define the host IP address or hostname
host = "www.google.com"

# ping the host 4 times and capture the output
ping_output = os.popen("ping -c 4 " + host).read()

# check if the host is reachable
if "4 packets transmitted, 4 received" in ping_output:
    print(host + " is reachable.")
else:
    print(host + " is not reachable.")
