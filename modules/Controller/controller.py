from modules.AIService.landmarkService import analyzeLandmark
from modules.Parser.landmarkResultParser import getNameFromLandmarkResults

def handleLandmarkImage():
    landmarkResults = analyzeLandmark()
    landmarkName = getNameFromLandmarkResults(landmarkResults)
    print(landmarkName)