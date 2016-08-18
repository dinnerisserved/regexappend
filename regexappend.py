import re, requests

s = requests.session()
response = s.get('http://url.com/')
r = s.get("http://url.com/")
print r.text
payload = r.text

randomnumb = re.findall(r"\{(.*?)\}", payload)
print randomnumb #just to check answer
print eval(*randomnumb) #just to check answer
result = eval(*randomnumb)
response = s.get("http://url.com/newpath/" + str(result))
print response.request.headers
print response.url
print response.text
print response.status_code
