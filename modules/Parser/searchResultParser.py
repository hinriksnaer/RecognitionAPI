def parseEntity(entitySearchResult):

    entitySearchResult = entitySearchResult['entities']['value'][0]

    dataObject = {}
    dataObject['thumbnailUrl'] = entitySearchResult['image']['thumbnailUrl']
    dataObject['discription'] = entitySearchResult['description']
    dataObject['wikiUrl'] = entitySearchResult['contractualRules'][1]['url']

    return dataObject

def getReleventLinksFromWebSearch(webSearchResult):

    webSearchResult = webSearchResult['webPages']['value']

    deepLinks = None

    for value in webSearchResult:
        if (value.get('deepLinks') != None):
            deepLinks = value['deepLinks']
        break

    return deepLinks