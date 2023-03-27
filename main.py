from proxylist import ProxyList
from revChatGPT.V1 import Chatbot
import requests
proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
pl = ProxyList.from_network_file(proxy_list_url)
proxy = pl.get_random_server().get_address()

url = "https://chat.openai.com/api/auth/session"
req = requests.get(url)
print(req.text)

# GPT = Chatbot(config={"session_token" "proxy": proxy})