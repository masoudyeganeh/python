import json
import requests
import csv
import jsondiff

dsCode = "90002"

def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

class Service:
    serviceName = ""
    baseFapiUrl = ""
    baseRestUrl = ""
    fapiCostumeUrl = ""
    restCostumeUrl = ""
    fapiQuery = ""
    fapiHeaders = ""
    fapiResponse = ""
    restHeaders = ""
    restResponse = ""

    def getFapiServiceUrl(self):
        return self.fapiCostumeUrl


customerInfo = Service()

baseFapiUrl = "https://fapi-test.irbroker.com"
fapiCostumeUrl = "/api/v1/customers/orders"

baseRestUrl = "http://192.168.2.201:9058"
restCostumeUrl = "/api/v1/customers/orders"

with open('mytestdata.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    testDatatList = list(reader)
    # print(nationalCode[1][0])

jsonDiff = []
for na in testDatatList:
    fapiQuery = {}
    fapiHeaders = {"x-fixed-token": "$2a$10$DrC65NU67gpcTIF7ez0U8udv3.kn8Lomm98RYEMy0DGYvxZ0GzW2S",
                   "X-CUSTOMER-ID": na[1], "x-ds-code": dsCode}
    fapiResponse = requests.get(baseFapiUrl + fapiCostumeUrl, headers=fapiHeaders, params=fapiQuery)
    print(fapiResponse.json())

    authQuery = {"username": "m.yeganeh", "password": "D1@yM25FKg2"}
    authHeaders = {"Content-Type": "application/json"}
    authResponse = requests.post(baseRestUrl + "/api/v1/authenticate", headers=authHeaders, json=authQuery)
    jsonResponse = authResponse.json()
    clientToken = jsonResponse['clientToken']

    customerInfoQuery = {"customerId": na[1], "dsCode": dsCode}
    customerInfoHeaders = {"X-CLIENT-TOKEN": clientToken}
    restResponse = requests.get(baseRestUrl + restCostumeUrl,
                                headers=customerInfoHeaders, params=customerInfoQuery)
    print(restResponse.json())
    from jsondiff import diff

    jsonDiff.append(diff(ordered(fapiResponse).json(), ordered(restResponse).json()))
print(jsonDiff)
