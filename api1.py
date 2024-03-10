import json
import requests

authQuery = {"username": "m.yeganeh", "password": "D1@yM25FKg2"}
restUrl = "http://192.168.2.201:9058/api/v1/"
authHeaders = {"Content-Type": "application/json"}
authResponse = requests.post(restUrl + "authenticate", headers=authHeaders, json=authQuery)
jsonResponse = authResponse.json()
clientToken = jsonResponse['clientToken']

customerInfoQuery = {"nationalCode": "10102968790", "dsCode": "811049"}
customerInfoHeaders = {"X-CLIENT-TOKEN": clientToken}
customerInfoResponse = requests.get(restUrl + "customers/customerInfo",
                                    headers=customerInfoHeaders, params=customerInfoQuery)
# print(customerInfoResponse.json())

fapiUrl = "https://fapi-test.irbroker.com"
fapiQuery = {"nationalCode": "4529719987", "isPortfo": "0", "prxCode": "", "lang": "fa"}
fapiHeaders = {"x-fixed-token": "$2a$10$DrC65NU67gpcTIF7ez0U8udv3.kn8Lomm98RYEMy0DGYvxZ0GzW2S",
               "X-CUSTOMER-ID": "10760003", "x-ds-code": "90001"}
fapiResponse = requests.get(fapiUrl + "/api/v1/customers/customerInfo", headers=fapiHeaders, params=fapiQuery)
print(fapiResponse.json())


