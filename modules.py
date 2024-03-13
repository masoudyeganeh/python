import applicationConfig as appConf
# from abc import ABC, abstractmethod
import requests
import pandas as pd


class Service:
    def __init__(self):
        self.name = ""
        self.fapiUrl = ""
        self.restUrl = ""
        self.fapiHeader = ""
        self.restHeader = ""
        self.fapiParams = ""
        self.restParams = ""
        self.jsonBody = ""

    def getFapiUrl(self):
        return appConf.baseFapiUrl + self.fapiUrl

    def getRestUrl(self):
        return appConf.baseRestUrl + self.restUrl

    def getRestHeaders(self):
        return {"X-CLIENT-TOKEN": getClientToken(appConf.username, appConf.password)}

    def getFapiHeaders(self):
        return self.fapiHeader

    def getFapiParams(self):
        return self.fapiParams

    def getRestParams(self):
        return self.restParams

    def setFapiParams(self, df, n):
        pass

    def setRestParams(self, df, n):
        pass

    def setFapiHeader(self, df, n):
        pass


class CustomerInfo(Service):
    def __init__(self):
        self.name = "customerInfo"
        self.fapiUrl = "customers/customerInfo"
        self.restUrl = "customers/customerInfo"
        self.fapiHeader = ""
        self.restHeader = ""
        self.fapiParams = ""
        self.restParams = ""
        self.jsonBody = ""

    def setFapiParams(self, df, n):
        self.fapiParams = {"nationalCode": str(df["nationalCode"][n]),
                           "isPortfo": "0", "prxCode": "", "lang": "fa"}

    def setFapiHeader(self, df, n):
        self.fapiHeader = {"x-fixed-token": appConf.fapiFixToken,
                           "X-CUSTOMER-ID": str(df["customerId"][n]), "x-ds-code": appConf.dsCode}

    def setRestParams(self, df, n):
        self.restParams = {"customerId": str(df["customerId"][n]), "dsCode": appConf.dsCode}


def getClientToken(u, p):
    authQuery = {"username": str(u), "password": str(p)}
    authHeaders = {"Content-Type": "application/json"}
    authResponse = requests.post(appConf.baseRestUrl + "authenticate", headers=authHeaders, json=authQuery)
    jsonResponse = authResponse.json()
    return jsonResponse['clientToken']


def getTestData():
    return pd.read_csv("mytestdata.csv")
