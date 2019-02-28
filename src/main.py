import ssl
from urllib import request
from bs4 import BeautifulSoup
import time

url = "http://www.air-level.com/"

context = ssl._create_unverified_context()
if __name__ == "__main__":
    response = request.urlopen(url, context=context)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    text_center = soup.find('div', class_='text-center')
    img_src = text_center.find('img')
    # print(text_center)
    # print(img_src)
    img_src = img_src.attrs['src']
    print(img_src)
    imgName = 0
    # f = open('D:\\Temp\\' + str(imgName) + ".jpg", 'wb')
    while 1 :
        update_time = text_center.find('h4').get_text()
        print(update_time)
        try:
            f = open('../img/' + update_time + ".png", 'wb')
            f.write((request.urlopen(img_src)).read())
            f.close()
        except Exception as e:
            print('download img error')
        time.sleep(1)
