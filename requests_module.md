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
- JSON 매개변수를 이용하여 요청 본문에 json 형식으로 추가됩니다. (dict의 형태를 띠어야 함)
> { 'key':'value', 'key1':'value1'}
- json 매개변수를 사용하면 요청 헤더에 기본적으로 Content-Type이 application/json 으로 지정된 상태로 요청이 된다.
```
r = requests.get("https://example.com", json={'test1':'jsondata2'})
print(r.request.headers)
# {'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '22', 'Content-Type': 'application/json'}

print(r.request.body)                 # b'{"test1": "jsondata2"}'
print(r.request.body.decode())        # {"test1": "jsondata2"}
```

### return
> put, get, post, head, patch, delete, options는 기본적으로 reqeusts.modules.Response 객체를 반환합니다.

## Request methods
> 전부다 return 해주는 값은 requests.request 함수이고 request의 인자에 PUT, GET등의 매개변수가 들어간다.
```
# 위 아래가 동일
r = requests.request('GET', url = 'htttps://example.com', params = {'get1':'value1',   'get2','value2'})
r = requests.get('https://example.com', params = {'get1':'value1',   'get2','value2'})
```

### PUT
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

### GET
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
### POST
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

### PATCH
> reqeusts.patch(url, data=None, **kwargs)
- 서버에게 resource의 업데이트를 요청합니다.
- PUT와 다른점은 찾는 key와 업데이트에 해당하는 부분만 바꾼다.
```
r = requests.patch("http://httpbin.org/patch", data={'patch1':'data1', 'patch2':'data2'})
print(r.request.method)                 # PATCH
print(r.request.body)                   # patch1=data1&patch2=data2
```

### DELETE
> requests.delete(url, **kwargs)
- 서버에게 resource의 삭제를 요청합니다.
```
r = reqeusts.delete("http://httpbin.org/delete")
print(r.request.method)                         # DELETE
```

## Response 객체
> HTTP 요청에 대한 서버의 응답을 포함한 객체입니다.
### methods
#### r.text
> text는 요청/응답 본문을 자동으로 디코드시킨 값을 str 타입으로 반환합니다.
```
r = requests.get("https://example.com")
print(r.text)
"""
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
...
"""
```

#### r.content
> content는 요청/응답 본문을 byte 타입으로 반환됩니다.
```
r = requests.get("https://exmaple.com")
print(r.content)
# b'<h1>Well hello there.</h1>\n<p>\nWelcome to exmaple.com.\n<br>Chances are you 
```

#### r.json()
> json()는 요청/응답 본문을 json 형식으로 디코딩하여 반환합니다. 만약 올바른 json 형식이 아닌 경우 에러를 반환합니다.
```
r = requests.get("https://example.com")
# print(r.json()) raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

r = requests.get("https://api.github.com/events")
print(r.json())
"""
[{'id': '23999925178', 'type': 'PushEvent', 'actor': {'id': 41898282, 'login': 'github-actions[bot]', 'display_login': 'github-actions', 'gravatar_id': '', 'url': 'https://api.github.com/users/github-actions[bot]', 'avatar_url': 'https://avatars.githubusercontent.com/u/41898282?'}, 'repo': {'id': 129699403, 'name': 'tuist/tuist', 'url': 'https://api.github.com/repos/tuist/tuist'}, 'payload': {'push_id': 11019469921, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/gh-pages', 'head': 'd8e4462281e7778e8367ceab719236af96affba5', 'before': '1d155f326528c1e5cc59a27ccea952deb8ab96d4', 'commits': [{'sha': 'd8e4462281e7778e8367ceab719236af96affba5', 'author': {'email': 'df@bendingspoons.com', 'name': 'danyf90'}, 'message': 'Deploying to gh-pages from @ tuist/tuist@3646b2830abebd3da768af69ec4c5a83c00ea667 🚀', 'distinct': True, 'url': 'https://api
"""
print(type(r.json()))               # <class 'list'>
```

### r.status_code
> status_code는 http 응답 코드를 나타냅니다. 요청에 성공한 경우 일반적으로 200을 반환합니다.
"""
r = requests.get("https://example.com")
print(r.status_code)                      # 200
"""



## Reference
[Reference] (https://me2nuk.com/Python-requests-module-example/)

[Reference] (https://steemit.com/url/@laon/url)

[Reference] (https://ko.eyewated.com/url%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C-%EC%9C%A0%EB%8B%88%ED%8F%BC-%EB%A6%AC%EC%86%8C%EC%8A%A4-%EB%A1%9C%EC%BC%80%EC%9D%B4%ED%84%B0/)

[Reference] (https://m.blog.naver.com/azure0777/220824614635)
