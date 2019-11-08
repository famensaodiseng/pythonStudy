import requests

tieba_name = input(":")

# 准备url
url_temp = "http://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"

# for i  in range(100):
#   url_list.append(url_temp.format(i+50))
url_list = [url_temp.format(i * 2) for i in range(10)]
print(url_list[:3])
# 发送请求

for url in url_list:
    resp = requests.get(url)

# 保存
file_path = "{}_第{}页.html".format(tieba_name, url_list.index(url) + 1)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(resp.content.decode())
