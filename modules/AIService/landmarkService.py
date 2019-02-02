import time 
import requests
import os
import operator
import numpy as np
from configparser import ConfigParser
from modules.request.request import processRequest


def analyzeLandmark():
    parser = ConfigParser()
    parser.read('config.ini')
    print(parser.get('DEFAULT', 'url'))
    url = parser.get('DEFAULT', 'Url')
    key = parser.get('DEFAULT', 'Key')

    # Load raw image file into memory
    pathToFileInDisk = f'./res/church.jpg'
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()
        
    # Computer Vision parameters
    params = { 'visualFeatures' : 'Color,Categories'} 

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = key
    headers['Content-Type'] = 'application/octet-stream'

    json = None

    result = processRequest( 'post', url, json, data, headers, params )

    return result
