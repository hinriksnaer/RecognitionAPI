from modules.AIService.landmarkService import analyzeLandmark
from modules.AIService.searchService import searchEntity, searchWeb
from modules.Parser.landmarkResultParser import getNameFromLandmarkResults
from modules.Parser.searchResultParser import parseEntity, getReleventLinksFromWebSearch

def handleLandmarkImage():
    data = {}

    landmarkResults = analyzeLandmark()
    landmarkName = getNameFromLandmarkResults(landmarkResults)
    
    entitySearchResults = searchEntity(searchParam)
    entity = parseEntity(entitySearchResults)

    webSearchResult = searchWeb(searchParam)
    deepLinks = getReleventLinksFromWebSearch(webSearchResult)

    data['name'] = landmarkName
    data['entity'] = entity
    data['releventLinks'] = deepLinks
    
    return data