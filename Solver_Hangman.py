#Hangman Solver

#Username: siyaofeng
#Password: daa9d0effc7021d4c9636094f211c748

import httplib
import json

conn = httplib.HTTPSConnection("hangman.leanapp.cn")

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nsiyaofeng\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\ndaa9d0effc7021d4c9636094f211c748\r\n-----011000010111000001101001--"

headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'authorization': "Basic c2l5YW9mZW5nOmRhYTlkMGVmZmM3MDIxZDRjOTYzNjA5NGYyMTFjNzQ4",
    'cache-control': "no-cache",
    'postman-token': "8acf63b3-68df-ff4a-3088-6c39a23c440a"
    }

conn.request("POST", "/login", payload, headers)

res = conn.getresponse()
data = res.read()

r1 = json.loads(data)
myToken = r1["token"]
print myToken
# print(data.decode("utf-8"))