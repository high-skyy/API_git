import requests

"""------------------put-----------------"""
"""
r = requests.put("http://httpbin.org/put", data={'put1':'data1', 'put2':'data2'})
print(r.request.method)
print(r.request.body)
"""
"""-------------------GET----------------"""
"""
r = requests.get("http://httpbin.org/get")
print(r.request.method)
print(r.url)
r = requests.get("http://httpbin.org/get", params={'data1':'value1','data2':'value2'})
print(r.url)
"""
"""-------------------POST----------------"""
"""
r = requests.post("http://httpbin.org/post", data = {'post1':'data1', 'post2':'data2'})
print(r.request.method)
print(r.request.body)
print(r.request.headers['Content-Type'])
r = requests.post("http://httpbin.org/post", json={'post1':'data1', 'post2':'data2'})
print(r.request.body)
print(r.request.headers['Content-Type'])
"""
"""-------------------PATCH----------------"""
"""
r = requests.patch("http://httpbin.org/patch", data={'patch1':'data1', 'patch2':'data2'})
print(r.request.method)
print(r.request.body)
"""
"""----------------json(dict)--------------"""
"""
r = requests.get("https://example.com", json={'test1':'jsondata2'})
print(r.request.headers)
print(r.request.body)
print(r.request.body.decode())
"""
"""-----------------r.text-------------"""
"""
r = requests.get("https://example.com")
print(r.text)
"""
"""------------------r.content-----------"""
"""
r = requests.get("https://exmaple.com")
print(r.content)
"""
"""-------------------r.json()-------------"""
"""
r = requests.get("https://example.com")
# print(r.json()) raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
r = requests.get("https://api.github.com/events")
print(r.json()[0])
print(type(r.json()))
"""


#[Reference] https://me2nuk.com/Python-requests-module-example/