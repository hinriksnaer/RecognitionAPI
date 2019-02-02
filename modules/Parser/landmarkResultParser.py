def getNameFromLandmarkResults(result):
    res = result['result']['landmarks'][0]['name']
    return res