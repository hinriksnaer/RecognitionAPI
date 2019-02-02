from flask import Flask, request, send_file

app = Flask(__name__)

imagefile = None      

# POST - just get the image and metadata
@app.route('/RequestImageWithMetadata', methods=['POST'])
def post():
    request_data = request.form['some_text']
    print(request_data)
    imagefile = request.files.get('imagefile', '')
    imagefile.save('D:/temp/test_image.jpg')
    return "OK", 200

app.run(port=5000)

@app.route('/get_image')
def get_image():
    imagefile = 'uploads\\123.jpg'
    return send_file(imagefile, mimetype='image/jpg')