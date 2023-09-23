# request 요청 해보기
import urllib.request
from http.client import HTTPConnection
from urllib.parse import urlencode

f = urllib.request.urlopen("http://www.google.com").read().decode("utf-8")

# GET 방식으로 URL 호출하기
host = "www.google.com"
conn = HTTPConnection(host)
conn.request('GET', '/')
r1 = conn.getresponse()
print(r1.status, r1.reason)
# 200 OK
conn.close()

# POST 방식으로 URL 호출하기
host = '127.0.0.1:8000'
params = urlencode({
    'language':'python',
    'name':'김석훈',
    'email':'shkim@naver.com'
})
headers={
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'text/plain'
}
conn=HTTPConnection(host)
conn.request('POST','',params,headers)
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.read()
print(data.decode('UTF-8'))
conn.close()