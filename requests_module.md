# requests_module
- python 사용자들을 위해 만들어진 간단한 Python용 HTTP 라이브러리, HTTPS 웹 사이트를 요청하기 위해 자주 사용되는 모듈
- Crawling 과정에서 requests 모듈을 이용해 웹 사이트의 소스코드를 가져온 다음 파싱을 하는 경우가 많다.
> (HTTP / Hyper text transfer protocol : 웹 상에서 통신을 하기 위한 규칙, 규약, 형식)

> Crawling : 웹페이지를 방문해서 자료를 수집하는 일을 하는 프로그램

## Request 매개변수

### url(필수)
> https://google.com

> URL(Uniform Resource Locators) : 인터넷상의 파일 위치를 식별하는 방법이다. HTTP또는 HTTPS 프로토콜을 사용하는 URL을 참조 할 때는 웹 사이트 주소라고도 한다.

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
> 전부다 return 해주는 값은 request의 함수이고 request의 인자에 PUT, GET등의 매개변수가 들어간다.
1. PUT
> requests.put(url, data=None, **kwargs)
- put메소드는 요청 시 PUT 방식으로 요청되며 data 매개변수를 지원합니다.
- data의 경우는 양식이 인코딩 되어 요청 본문에 추가된다.
- 서버에게 resource의 업데이트를 하거나 resource가 없다면 새로운 resource를 생성해 달라고 합니다.
- (PATCH)와 비교해서는 전체 데이터를 교체하는 차이가 있다.
```
r = requests.put("http://httpbin.org/put", data={'put1':'data1', 'put2':'data2'})
print(r.request.method)      # 'PUT'
print(r.request.body)        # 'put1=data1&put2=data2'
```

2. GET
> requests.get(url, params=None, **kwargs)
- get메소드는 요청 시 GET 방식으로 요청되며 params 매개변수를 지원합니다.
- params는 양식이 인코딩 되어 url에 추가된다.
- 서버에게 resource를 보내달라고 요청합니다.
```
r = requests.get("http://httpbin.org/get")
print(r.request.method)
print(r.url)
r = requests.get("http://httpbin.org/get", params={'data1':'value1','data2':'value2'})
print(r.url)
```
3. POST
> requests.post(url, data=None, json=None, **kwargs)
- data랑 json 모두 요청 본문에 추가됨 (하지만 요청할 때 헤더의 Content-Type이 달라진다.)
- 서버에게 resource를 보내면서 생성해 달라고 요청합니다.
```
r = requests.post("http://httpbin.org/post", data = {'post1':'data1', 'post2':'data2'})
print(r.request.method)                     # POST
print(r.request.body)                       # post1=data1&post2=data2
print(r.request.headers['Content-Type'])    # application/x-www-form-urlencoded
r = requests.post("http://httpbin.org/post", json={'post1':'data1', 'post2':'data2'})
print(r.request.body)                       # b'{"post1": "data1", "post2": "data2"}'
print(r.request.headers['Content-Type'])    # application/json
```

4. PATCH
> reqeusts.patch(url, data=None, **kwargs)
- 서버에게 resource의 업데이트를 요청합니다.
- PUT와 다른점은 찾는 key와 업데이트에 해당하는 부분만 바꾼다.
```
r = requests.patch("http://httpbin.org/patch", data={'patch1':'data1', 'patch2':'data2'})
print(r.request.method)                 # PATCH
print(r.request.body)                   # patch1=data1&patch2=data2
```

5. DELETE
> requests.delete(url, **kwargs)
- 서버에게 resource의 삭제를 요청합니다.
```
r = reqeusts.delete("http://httpbin.org/delete")
print(r.request.method)                         # DELETE
```




## Reference
[Reference] (https://me2nuk.com/Python-requests-module-example/)
[Reference] (https://steemit.com/url/@laon/url)
[Reference] (https://ko.eyewated.com/url%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C-%EC%9C%A0%EB%8B%88%ED%8F%BC-%EB%A6%AC%EC%86%8C%EC%8A%A4-%EB%A1%9C%EC%BC%80%EC%9D%B4%ED%84%B0/)
[Reference] (https://m.blog.naver.com/azure0777/220824614635)
