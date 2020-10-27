"""
sample
http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?serviceKey=[secret key]
"""

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body


