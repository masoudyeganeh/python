import requests
import generalMethods
import applicationConfig as appConf


class CustomerInfo(generalMethods.Service):
    def __init__(self):
        super().__init__()
        self.name = "customerInfo"
        self.fapiUrl = "customers/customerInfo"
        self.restUrl = "customers/customerInfo"
        self.fapiHeader = ""
        self.restHeader = ""
        self.fapiParams = ""
        self.restParams = ""
        self.jsonBody = ""
        self.fapiResponse = ""
        self.restResponse = ""

    def setFapiParams(self, df, n):
        self.fapiParams = {"nationalCode": str(df["nationalCode"][n]),
                           "isPortfo": "0", "prxCode": "", "lang": "fa"}

    def setFapiHeader(self, df, n):
        self.fapiHeader = {"x-fixed-token": appConf.fapiFixToken,
                           "X-CUSTOMER-ID": str(df["customerId"][n]), "x-ds-code": appConf.dsCode}

    def setRestParams(self, df, n):
        self.restParams = {"customerId": str(df["customerId"][n]), "dsCode": appConf.dsCode}


def makeCustomerInfo():
    customerInfo = CustomerInfo()
    return customerInfo


def callCustomerInfoAPI(customerinfo):
    df = generalMethods.getTestData()
    n = 0

    for i in df:
        n = n + 1
        customerinfo.setFapiParams(df, n)
        customerinfo.setFapiHeader(df, n)
        customerinfo.setRestParams(df, n)
        fapiResponse = requests.get(customerinfo.getFapiUrl(),
                                    headers=customerinfo.getFapiHeaders(), params=customerinfo.getFapiParams())

        restResponse = requests.get(customerinfo.getRestUrl(),
                                    headers=customerinfo.getRestHeaders(), params=customerinfo.getRestParams())
        customerinfo.setFapiResponse(fapiResponse.json())
        customerinfo.setRestResponse(restResponse.json())
    return

