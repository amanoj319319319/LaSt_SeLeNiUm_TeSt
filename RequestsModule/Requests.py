'''
import requests
import json
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print (type(r))
print (r.status_code)
#print (r.text)
info=r.json()
print (type(info))
print (info)

'''

'''
import requests
import json
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print (type(r))
print (r.status_code)
print (r.text)
'''

'''
import requests
import json
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print (type(r))
print (r.status_code)
print (r.content)
'''

'''
import requests
import json
import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print (type(r))
print (r.status_code)
print (r.text)
print (r.headers)
print (r.headers['Content-Type'])
'''

'''
# importing the requests library
import requests

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

print (data)
'''


#PART-1
'''
import pdb
import requests
url="https://reqres.in/api/users?page=2"
pdb.set_trace()
response = requests.get(url)
print (type(response))
print (response.content)
print ("********************")
print (response.text)
print ("********************")
print (response.headers)
print ("********************")
print (response.cookies)
#PART-2
'''

'''
import requests
import  json
import jsonpath
url="https://reqres.in/api/users?page=2"
response = requests.get(url)#we get response in the form of json string format
print ("********************")
json_response = json.loads(response.text)#we converted json string format into python dict using json,loads()
print (type(json_response))
print (json_response)
pages=jsonpath.jsonpath(json_response,"total")
print (pages)
assert pages[0]==12
print (response.headers)
print ("********************")
print (response.cookies)
'''

#PART-3 ...DELETING A USER
'''
import requests
import  json
import jsonpath
url="https://reqres.in/api/users/2"
responce = requests.delete(url)
print (responce.status_code)
assert responce.status_code==204
'''

#PART-4 POST
'''
import requests
import  json
import jsonpath
url="https://reqres.in/api/users"

#Read input Json file
file = open("C:\\Users\\Manoj\\Desktop\\Create.json")
json_input=file.read()
request_json=json.loads(json_input)

#Make post request with json input body
response = requests.post(url,request_json)
print (response.status_code)
print (type(response))
print (response.text)
assert response.status_code==201
print ("headers are .......................")
headers=response.headers
print (headers)
print ("want to get a particular header value ........")
print (headers.get('Content-Type'))

#parse response to json format
response_json=json.loads(response.text)
print (response_json)

#pick id using jsonpath
id=jsonpath.jsonpath(response_json,"id")#everytime new id will be generated from the server .in the new source will be created
print (id[0])

'''

#PART-5 PUT REQUEST
'''
import requests
import  json
import jsonpath
url="https://reqres.in/api/users/2"

#Read input Json file
file = open("C:\\Users\\Manoj\\Desktop\\Create.json")
json_input=file.read()
request_json=json.loads(json_input)

#Make PUT request with json input body
response = requests.put(url,request_json)
print (response.status_code)
print (type(response))
print (response.text)
assert response.status_code==200
print ("headers are .......................")
headers=response.headers
print (headers)
print ("want to get a particular header value ........")
print (headers.get('Content-Type'))

#parse response to json format
response_json=json.loads(response.text)
print (response_json)

#pick id using jsonpath
id=jsonpath.jsonpath(response_json,"name")#everytime new id will be generated from the server .in the new source will be created
print (id[0])

'''

