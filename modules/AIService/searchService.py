from configparser import ConfigParser
from modules.request.request import processRequest
import urllib

def searchEntity(searchString):
    parser = ConfigParser()
    parser.read('config.ini')
    url = parser.get('DEFAULT', 'SearchUrl') + '/entities'
    key = parser.get('DEFAULT', 'SearchKey')

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = key
    mkt = 'en-US'
    params = '?mkt=' + mkt + '&q=' + urllib.parse.quote (searchString)

    result = processRequest( 'get', url + params, headers = headers)
    return result

def searchWeb(searchString):
    parser = ConfigParser()
    parser.read('config.ini')
    url = parser.get('DEFAULT', 'SearchUrl') + '/search'
    key = parser.get('DEFAULT', 'SearchKey')

    headers = {"Ocp-Apim-Subscription-Key" : key}
    params  = {"q": searchString, "textDecorations":True, "textFormat":"HTML"}
    result = processRequest('get', url, params = params, headers = headers)
    return result
    
