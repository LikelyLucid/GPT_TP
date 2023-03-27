from pychatgpt import Chat, Options
from proxylist import ProxyList
options = Options()
proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
pl = ProxyList.from_network_file(proxy_list_url)
proxy = f"http://{pl.get_random_server().get_address()}"
print(proxy)
# options.proxies = proxy
email = "micool.plays@gmail.com"
password = "micooliscool"
# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
chat = Chat(email=email, password=password, options=options)
answer = chat.ask("How are you?")
print(answer)