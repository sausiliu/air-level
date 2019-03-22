import ssl
from urllib import request
from bs4 import BeautifulSoup
import time
import schedule
from urllib.request import urlretrieve
from imp import reload

url = "http://www.air-level.com/"
context = ssl._create_unverified_context()

def download_img():
    response = request.urlopen(url, context=context)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    text_center = soup.find('div', class_='text-center')
    img_src = text_center.find('img')
    # print(text_center)
    # print(img_src)
    img_src = img_src.attrs['src']
    print(img_src)
    # img_name = 0

    #time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    time_str = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
    png_name = time_str + '.png'
    try:
        print('xxxxx')
        #f = open('../img/' + time_str + ".png", 'wb+')
        #f.write((request.urlopen(img_src)).read())
        #f.close()
        urlretrieve(img_src, png_name)
    except Exception as e:
        print('download img error:' + str(e))

    time.sleep(1)

download_img()
# schedule.every().hour.do(download_img)
schedule.every(3).seconds.do(download_img)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)

