from proxylist import ProxyList
from revChatGPT.V1 import Chatbot
import requests

proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
pl = ProxyList.from_network_file(proxy_list_url)
proxy = pl.get_random_server().get_address()
email = "micool.plays@gmail.com"
password = "micooliscool"
GPT = Chatbot(config={"email": email, "password": password, "proxy": proxy})
prompt = "how many beaches does portugal have?"
response = ""

for data in GPT.ask(prompt):
    response = data["message"]

print(response)
