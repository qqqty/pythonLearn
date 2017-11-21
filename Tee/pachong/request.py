
import requests

url = "https://github.com/timeline.json"
# # get
# res = requests.get(url)
#
# payLoad = {'age':'23', 'sex':'male'}
# resT = requests.get(url, params=payLoad)
#
# print res.url, res.text
# print resT.url, resT.text
#


# post
args = {'nameTmp':'test', 'pw':'123'}
headers = {'content-type':'application/json'}
res = requests.post(url, data=args, headers=headers)

print res.url
print res.text
print res.cookies













