'''
import requests
import  json
import jsonpath
import pytest
url="https://reqres.in/api/users"

def test_creating_firstuser():
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


def test_creating_seconduser():
    #Read input Json file
    file = open("C:\\Users\\Manoj\\Desktop\\Create2.json")
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
