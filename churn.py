import json
import requests
from abc import ABC, abstractmethod
import csv
import pandas as pd

df = pd.read_csv("testData.csv")

baseRestUrl = "http://192.168.2.201:9058/api/v1/"
baseFapiUrl = "https://fapi-test.irbroker.com/api/v1/"

username = "m.yeganeh"
password = "D1@yM25FKg2"

fapiFixToken = "$2a$10$DrC65NU67gpcTIF7ez0U8udv3.kn8Lomm98RYEMy0DGYvxZ0GzW2S"
dsCode = "90002"


def getClientToken(u, p):
    authQuery = {"username": str(u), "password": str(p)}
    authHeaders = {"Content-Type": "application/json"}
    authResponse = requests.post(baseRestUrl + "authenticate", headers=authHeaders, json=authQuery)
    jsonResponse = authResponse.json()
    return jsonResponse['clientToken']


class Service(ABC):
    name: ""
    fapiUrl: ""
    restUrl: ""
    fapiHeader: ""
    restHeader: ""
    fapiParams: ""
    restParams: ""
    jsonBody: ""

    def getFapiUrl(self):
        return baseFapiUrl + self.fapiUrl

    def getRestUrl(self):
        return baseRestUrl + self.restUrl

    def getRestHeaders(self):
        return {"X-CLIENT-TOKEN": getClientToken(username, password)}

    def getFapiHeaders(self):
        return self.fapiHeader

    def getFapiParams(self):
        return self.fapiParams

    def getRestParams(self):
        return self.restParams

    @abstractmethod
    def setFapiParams(self):
        pass

    @abstractmethod
    def setRestParams(self):
        pass

    @abstractmethod
    def setFapiHeader(self):
        pass


class CustomerInfo(Service):
    def __init__(self):
        self.name = "customerInfo"
        self.fapiUrl = "cusromers/customerInfo"
        self.restUrl = "customers/customerInfo"


    def setFapiParams(self, n):
        self.fapiParams = {"nationalCode": str(df["nationalCode"][n]),
                           "isPortfo": "0", "prxCode": "", "lang": "fa"}

    def setFapiHeader(self,n):
        self.fapiParams = {"x-fixed-token": fapiFixToken,
                           "X-CUSTOMER-ID": str(df["customerId"][n]), "x-ds-code": dsCode}

    def setRestParams(self):
        self.restParams = {"customerId": str(df["customerId"][n]), "dsCode": dsCode}


customerInfo = CustomerInfo()
n = 0

for i in df:
    n = n + 1
    customerInfo.setFapiParams(n)
    a = customerInfo.getFapiParams()
    fapiResponse = requests.get(customerInfo.getFapiUrl(),
                                headers=customerInfo.getFapiHeaders(), params=customerInfo.getFapiParams())

    restResponse = requests.get(customerInfo.getRestUrl(),
                                headers=customerInfo.getRestHeaders(), params=customerInfo.getRestParams())

