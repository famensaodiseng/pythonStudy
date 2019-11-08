import time
import requests
print("ok")
url = "http://www.itcast.cn/2018czgw/images/logo.png"
response  = requests.get(url)
with open ("itcast.png","wb") as f:
    f.write(response.content)