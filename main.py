import requests
import random
proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
req = requests.get(proxy_list_url)

#print random line of txt from request
print(req)