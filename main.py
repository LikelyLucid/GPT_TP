from proxylist import ProxyList
from revChatGPT.V1 import Chatbot

proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
pl = ProxyList.from_network_file(proxy_list_url)
proxy = pl.get_random_server().get_address()

email = "micoolplays2@gmail.com"
password = ""

GPT = Chatbot(config={"email": email, "password": password, "proxy": proxy})