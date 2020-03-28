import requests
import json
import jsonpath



def test_AddNewStudent():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    f=open('C:/Users/Admin/PycharmProjects/APIautomationPytest/student.json', 'r')
    json_req=json.loads(f.read())
    response=requests.post(API_URL,json_req)
    print(response.text)

def test_GetStudent():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/163149"
    #f=open('C:/Users/Admin/PycharmProjects/APIautomationPytest/student.json', 'r')
    #json_req=json.loads(f.read())
    response=requests.get(API_URL)
    json_response=response.json()
    id=jsonpath.jsonpath(json_response,'data.id')
    assert id[0]==163149
    #print(response.text)

