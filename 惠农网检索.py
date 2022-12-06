import csv
import requests
from bs4 import BeautifulSoup
import re
import cv2 as cv

with open('244.csv',encoding='utf-8')as fp:
    reader = csv.reader(fp)
    # 获取标题
    # header = next(reader)
    # print(reader)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
    for item in reader:
        for j in range(len(item)):
            url = 'https://www.cnhnb.com'+item[j]
            # url = 'https://www.cnhnb.com/hangqing/cdlist-2000586-604/'
            # print(url)
            message = requests.get(url,headers=headers)
            soup = BeautifulSoup(message.text,'lxml')
            if soup.title.string == '请验证':
                print(message.url)
                break
            else:
                mess = []
                mess_dict = {}
                for ul in soup.select('.product')[1:]:
                    mess_dict['产品']=ul.get_text()
                    mess.append(mess_dict.copy())
                for ul in soup.select('.place')[1:]:
                    mess_dict['所在地']=ul.get_text()
                    mess.append(mess_dict.copy())
                for ul in soup.select('.price')[1:]:
                    mess_dict['价格']=ul.get_text()
                    mess.append(mess_dict.copy())
                mess1 = []
                for i in mess:
                    if len(i) == 3:
                        mess1.append(i)
                # print(mess1)
                #写入文件
                # if soup.title.string == '请验证'：
                #     for i
                header = ['产品','所在地','价格']
                with open('惠农网信息.csv', 'a+', encoding='utf-8', newline='') as fp:
                    # 写
                    writer = csv.DictWriter(fp, header)
                    # # 写入标题
                    # writer.writeheader()
                    # 将数据写入
                    writer.writerows(mess1)
                    fp.close()
