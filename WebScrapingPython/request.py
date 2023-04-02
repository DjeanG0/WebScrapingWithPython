import requests

url = 'https://www.classcentral.com'
web = requests.get(url)

web.status_code
print(web.text) #print html code
print(web.content)
web.headers      #header request 
web.request.headers  #header request
web.request.method     #type of method
web.request.url       #url of request