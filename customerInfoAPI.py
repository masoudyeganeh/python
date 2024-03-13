import requests
import modules
from jsondiff import diff


def callCustomerInfoAPI():
    df = modules.getTestData()
    customerInfo = modules.CustomerInfo()
    n = 0

    jsonDiff = []

    for i in df:
        n = n + 1
        customerInfo.setFapiParams(df, n)
        customerInfo.setFapiHeader(df, n)
        customerInfo.setRestParams(df, n)
        u = customerInfo.getRestUrl()
        h = customerInfo.getRestHeaders()
        p = customerInfo.getRestParams()
        fapiResponse = requests.get(customerInfo.getFapiUrl(),
                                    headers=customerInfo.getFapiHeaders(), params=customerInfo.getFapiParams())

        restResponse = requests.get(customerInfo.getRestUrl(),
                                    headers=customerInfo.getRestHeaders(), params=customerInfo.getRestParams())
        print(fapiResponse)
        print(restResponse)
        jsonDiff.append(diff(fapiResponse.json(), restResponse.json()))
    return jsonDiff
