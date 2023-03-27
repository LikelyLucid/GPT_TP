from proxylist import ProxyList
from revChatGPT.V1 import Chatbot
import requests
proxy_list_url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
pl = ProxyList.from_network_file(proxy_list_url)
proxy = pl.get_random_server().get_address()

sess_id = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJtaWNvb2xwbGF5czJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItQWxlY1RrSFRPVDZLbTZOSkxadXRLOEpQIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2MmVjNTc3ZDljNmM2ZGU1NjExNzcxYTEiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc4NTg1NzQ2LCJleHAiOjE2Nzk3OTUzNDYsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb2ZmbGluZV9hY2Nlc3MifQ.X3deUXVXSZCzek1FdJChsE9v10FH9E1cWgKAefRYtR_oqERCn-n1FuSwewoHoJ7GxYsBOgjG2dxnuW8NKTpxxMSFxeoK8CwnyVT7oM8vArGVbs5-GGEyvfnJ1ccR7i-p2zk9IYZTo758yT1uU2Yp8_uVyHo5oazHgCWI7HZqaocUNCvbSr7h-QZrVmz-5AWyzKB0GhoSKH-y4q3YCSwQL5zA8eJhckfA6XW-P54DsW_OFC_MYasF_IdckTcthP93u4DIGs6leslwGI0QEZYRtdFkBR8pG5_X_zX2EQIO1p1EU6KN9qGMaHrZI3O5NFuyJttssTC2hfmFvw-8RnWFkQ"

GPT = Chatbot(config={"access_token": sess_id, "proxy": proxy})
prompt = "how many beaches does portugal have?"
response = ""

for data in GPT.ask(
  prompt
):
    response = data["message"]

print(response)