from flask import Flask, request

app = Flask(__name__)        

# POST - just get the image and metadata
@app.route('/RequestImageWithMetadata', methods=['POST'])
def post():
    request_data = request.form['some_text']
    print(request_data)
    imagefile = request.files.get('imagefile', '')
    imagefile.save('D:/temp/test_image.jpg')
    return "OK", 200

app.run(port=5000)