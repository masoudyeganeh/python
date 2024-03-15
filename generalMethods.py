import applicationConfig as appConf
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
        self.fapiResponse = ""
        self.restResponse = ""

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

    def getFapiResponse(self):
        return self.fapiResponse

    def getRestResponse(self):
        return self.restResponse

    def setFapiParams(self, df, n):
        pass

    def setRestParams(self, df, n):
        pass

    def setFapiHeader(self, df, n):
        pass

    def setFapiResponse(self, r):
        self.fapiResponse = r

    def setRestResponse(self, r):
        self.restResponse = r

    def getFapiKeys(self):
        get_keys(self.getFapiResponse)

    def getRestKeys(self):
        get_keys(self.getRestResponse())


def getClientToken(u, p):
    authQuery = {"username": str(u), "password": str(p)}
    authHeaders = {"Content-Type": "application/json"}
    authResponse = requests.post(appConf.baseRestUrl + "authenticate", headers=authHeaders, json=authQuery)
    jsonResponse = authResponse.json()
    return jsonResponse['clientToken']


def getTestData():
    return pd.read_csv("mytestdata.csv")


def get_keys(d):
    if isinstance(d, dict):
        for k, v in d.items():
            yield k
            yield from list(get_keys(v))
    elif isinstance(d, list):
        for o in d:
            yield from list(get_keys(o))


def count_keys(d):
    c = 0
    if isinstance(d, dict):
        for k, v in d.items():
            c = c + 1
            yield c
            yield from list(count_keys(v))
    elif isinstance(d, list):
        for o in d:
            yield from list(count_keys(o))
