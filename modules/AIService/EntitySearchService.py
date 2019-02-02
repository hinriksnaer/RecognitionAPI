from configparser import ConfigParser
from modules.request.request import processRequest
import urllib

def searchEntity(searchString):
    parser = ConfigParser()
    parser.read('config.ini')
    url = parser.get('DEFAULT', 'EntitySearchUrl')
    key = parser.get('DEFAULT', 'SearchKey')

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = key
    mkt = 'en-US'
    params = '?mkt=' + mkt + '&q=' + urllib.parse.quote (searchString)

    result = processRequest( 'get', url + params, headers = headers)
    print(result)
    return result