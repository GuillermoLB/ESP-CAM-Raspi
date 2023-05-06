from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'imageFile' in request.files:
        image = request.files['imageFile']
        image.save('received_image.jpg')
        return 'Image received'
    else:
        return 'No image received'
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)