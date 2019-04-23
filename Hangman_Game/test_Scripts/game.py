import httplib2
import urllib
data = {'name': 'fred', 'address': '123 shady lane'}
body = urllib.parse.urlencode(data)
h = httplib2.Http()
resp, content = h.request("http://192.168.0.102:8000", method="POST", body=body)
