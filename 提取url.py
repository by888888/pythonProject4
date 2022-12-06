import csv
import requests
from bs4 import BeautifulSoup
import re
import cv2 as cv

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
url = 'https://www.cnhnb.com/hangqing/sczw/'
            # print(url)
message = requests.get(url,headers=headers)
soup = BeautifulSoup(message.text,'lxml')
if soup.title.string == '请验证':
    print(message.url)
# print(soup.select('a[class="third-cate-item link-expanded"]'),'\n')
# links = soup.select('a[class="third-cate-item link-expanded"]')
links = soup.select('a[class="third-cate-item link-expanded"]')
# 获取每个元素中'href'键对应的键值--即URL，并放入url_lst
m = []
for j in p:
    u = j.get('href')
    m.append(u)
url_lst1 = list(set(m))
print(url_lst1)
url_lst = []
for i in range(len(links)):
    # u = i.get('href').split('-',3)
    # m = (u[0] + '-' + u[1] + '-' + u[2] + '/')
    # url_lst.append(m)
    # u = i.get('href')
    if '-' in links[i]:
        url_lst.append(i)
p = [links[i] for i in range(len(links)) if (i not in links)]

# for j in url_lst1:
#     if '-' in
# print(url_lst1)



# output = open('website.csv', 'a+', newline='')
# writer = csv.writer(output)
# for row in url_lst1:
#     if row:  # 去除空行
#         writer.writerow([row])
# print("保存文件成功，处理结束")

