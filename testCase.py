import generalMethods


def compareKeys(object):
    fapiKeys = list(dict.fromkeys(list(object.getFapiKeys())))
    restKeys = list(dict.fromkeys(list(object.getFapiKeys())))
    if fapiKeys == restKeys:
        return
    else:
        return list(set(fapiKeys) - set(restKeys))

