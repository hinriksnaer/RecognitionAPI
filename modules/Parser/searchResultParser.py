def parseEntity(entitySearchResult):

    entitySearchResult = entitySearchResult['entities']['value'][0]

    dataObject = {}
    dataObject['wikiUrl'] = entitySearchResult['contractualRules'][1]['url']
    dataObject['thumbnailUrl'] = entitySearchResult['image']['thumbnailUrl']
    dataObject['discription'] = entitySearchResult['description']

    return dataObject

def getReleventLinksFromWebSearch(webSearchResult):

    webSearchResult = webSearchResult['webPages']['value']

    deepLinks = None

    for value in webSearchResult:
        if (value.get('deepLinks') != None):
            deepLinks = value['deepLinks']
        break

    return deepLinks