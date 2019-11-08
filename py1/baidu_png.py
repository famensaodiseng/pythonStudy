import requests

url = "https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png"
response  = requests.get(url)

with open ("baidu.png","wb") as f:
    f.write(response.content)