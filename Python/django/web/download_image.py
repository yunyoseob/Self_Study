import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs): # 이미지 태그 찾기
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result=[]
        for name, value in attrs:
            if name == 'src': # <img src 찾기
                self.result.append(value)
    
def download_image(url, data):
    if not os.path.exists('DOWNLOAD'):
        os.makedirs('DOWNLOAD')
    parser = ImageParser() 
    parser.feed(data) # HTML 문장을 feed() 함수에 주면, 바로 파싱하고 그 결과를 parser.result에 추가합니다.
    dataSet = set(x for x in parser.result)
    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join('DOWNLOAD', basename)
        print("Downloading...", imageUrl)
        urlretrieve(imageUrl, targetFile)

def main():
    host = "www.google.co.kr"
    conn = HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()
    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()
    print("\n >>>>>> Download Images from", host)
    url = urlunparse(('http',host, '','','',''))
    print("main:: url >>> ", url)
    download_image(url, data)

if __name__ == '__main__':
    main()