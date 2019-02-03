from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json
import base64
from modules.Controller.controller import handleLandmarkImage

app = Flask(__name__)
api = Api(app)

with open('description.json') as f:
    data = json.load(f)


#Function used to send error if id does not exist
def abort_if_image_doesnt_exist(image_arg):
    if 'imgText' not in image_arg:
        abort(404, message="Image {} doesn't exist".format(image_arg))

#init parser
parser = reqparse.RequestParser()
#Makes it a must to include a imgText param in the request
parser.add_argument('imgText', type=str)


class dummyRead(Resource):
    def get(self):
        dummyFile = open('tett.txt', 'r')
        dummyFile = base64.b64decode(dummyFile.read())
        filename = './temp/image_to_analyze.png'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(dummyFile)
        results = handleLandmarkImage()
        return results, 201, {'Content-Type': 'application/json;charset=utf-8'}

class ConvertImage(Resource):
    def post(self):
        print('Attempting to convert image...')
        try:
            args = parser.parse_args()
            imgstring = {'imgText' : args['imgText']}
            imgdata = base64.b64decode(imgstring['imgText'])
            filename = './temp/image_to_analyze.png'  # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
            results = handleLandmarkImage()
            return results, 201, {'Content-Type': 'application/json;charset=utf-8'}
        except Exception:
            abort(404, message="Something went wrong")

class ImageList(Resource):
    def get(self):
        return data

    def post(self):
        args = parser.parse_args()
        image_id = int(max(data.keys()).lstrip('todo')) + 1
        image_id = 'todo%i' % image_id
        data[image_id] = {'task': args['task']}
        return data[image_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(ImageList, '/')
api.add_resource(ConvertImage, '/imagepost')
api.add_resource(dummyRead, '/dummy')
#api.add_resource(Todo, '/todos/<todo_id>')
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
