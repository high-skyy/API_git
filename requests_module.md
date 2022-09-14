# requests_module
- python 사용자들을 위해 만들어진 간단한 Python용 HTTP 라이브러리, HTTPS 웹 사이트를 요청하기 위해 자주 사용되는 모듈
- Crawling 과정에서 requests 모듈을 이용해 웹 사이트의 소스코드를 가져온 다음 파싱을 하는 경우가 많다.
> (HTTP / Hyper text transfer protocol : 웹 상에서 통신을 하기 위한 규칙, 규약, 형식)

> Crawling : 웹페이지를 방문해서 자료를 수집하는 일을 하는 프로그램

## Request 매개변수

### url(필수)
> https://google.com
### params(선택 사항)
tuple, dict 형식으로 매개변수에 넣으면 양식이 URL 인코딩이 되어 URL에 추가됩니다.
> URL?key=value&key1=value
### data(선택 사항)
tuple, dict 형식으로 매개변수에 넣으면 양식이 인코딩되어 요청 본문에 추가됩니다.
> key=value&key1=value1
### JSON(선택 사항)
JSON 매개변수를 이용하여 요청 본문에 json 형식으로 추가됩니다.
> { 'key':'value', 'key1':'value1'}
### return
> put, get, post, head, patch, delete, options는 기본적으로 reqeusts.modules.Response 객체를 반환합니다.

## Request methods
1. PUT
> requests.put(url, data=None, **kwargs)
- put메소드는 요청 시 PUT 방식으로 요청되며 data 매개변수를 지원합니다.
- data의 경우는 양식이 인코딩 되어 요청 본문에 추가된다.
```
r = requests.put("http://httpbin.org/put", data={'put1':'data1', 'put2':'data2'})
print(r.request.method)      # 'PUT'
print(r.request.body)        # 'put1=data1&put2=data2'
```

2. GET
> requests.get(url, params=None, **kwargs)
- get메소드는 요청 시 GET 방식으로 요청되며 params 매개변수를 지원합니다.
- params는 양식이 인코딩 되어 url에 추가된다.
```
r = requests.get("http://httpbin.org/get")
print(r.request.method)
print(r.url)
r = requests.get("http://httpbin.org/get", params={'data1':'value1','data2':'value2'})
print(r.url)
```
3. POST
> requests.post(url, data=None, json=None, **kwargs)
```
def post(url, data=None, json=None, **kwargs):
    [...]
    return request('post', url, data=data, json=json, **kwargs)
```





## Reference
[Reference] (https://me2nuk.com/Python-requests-module-example/)
