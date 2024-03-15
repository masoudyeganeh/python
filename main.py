import customerInfoAPI
import testCase

customerInfo = customerInfoAPI.makeCustomerInfo()
customerInfoAPI.callCustomerInfoAPI(customerInfo)

compareKeysTestResult = testCase.compareKeys(customerInfo)


