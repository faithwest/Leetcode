import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("5y2v5g.api.infobip.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=from;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("faithngeno7@gmail.com"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=subject;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("Free trial"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=to;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("{\"to\":\"faithngeno7@gmail.com\",\"placeholders\":{\"firstName\":\"Faith\"}}"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=text;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("Hi {{firstName}}, this is a test message from Infobip. Have a nice day!"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
    'Authorization': 'App 5fc7ab255439b9869822123d397670ce-90bd0e5d-2226-4758-aadd-216c74262580',
    'Accept': 'application/json',
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/email/3/send", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))