from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

with open('description.json') as f:
    data = json.load(f)


#Function used to send error if id does not exist
def abort_if_image_doesnt_exist(image_id):
    if image_id not in data:
        abort(404, message="Todo {} doesn't exist".format(image_id))

#init parser
parser = reqparse.RequestParser()

#Makes it a must to include a task param in the request
#parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, image_id):
        abort_if_image_doesnt_exist(image_id)
        return data[image_id]

    def delete(self, image_id):
        abort_if_image_doesnt_exist(image_id)
        del data[image_id]
        return '', 204

    def put(self, image_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        data[image_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
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
#api.add_resource(Todo, '/todos/<todo_id>')
if __name__ == '__main__':
    #app.run(debug=True)
    app.run()