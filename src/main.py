import ssl
from urllib import request
from bs4 import BeautifulSoup

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
    # f = open('D:\\Temp\\' + str(imgName) + ".jpg", 'wb')
