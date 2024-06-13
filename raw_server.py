from flask import Flask, request, send_file
from datetime import datetime
import os
import zipfile

app = Flask(__name__)

def get_mode():
    print("Select a mode:")
    print("1. Save image as 'received_image.jpg' in 'image' folder")
    print("2. Save image with timestamp in 'archive' folder")
    mode = input("Enter the number of your selected mode: ")
    return mode

mode = get_mode()

@app.route('/upload', methods=['POST'])
def upload():
    if 'imageFile' in request.files:
        image = request.files['imageFile']
        if mode == '1':
            os.makedirs('image', exist_ok=True)
            image_path = os.path.join('image', 'received_image.jpg')
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.makedirs('archive', exist_ok=True)
            image_path = os.path.join('archive', f'{timestamp}.jpg')
        image.save(image_path)
        return 'Image received and saved'
    else:
        return 'No image received'

@app.route('/download_archive', methods=['GET'])
def download_archive():
    # Create a ZipFile object
    with zipfile.ZipFile('archive.zip', 'w') as zipf:
        # Iterate over all the files in the 'archive' directory
        for foldername, subfolders, filenames in os.walk('archive'):
            for filename in filenames:
                # Create complete filepath of file in directory
                filepath = os.path.join(foldername, filename)
                # Add file to zip
                zipf.write(filepath)
    return send_file('archive.zip', as_attachment=True)

@app.route('/download', methods=['GET'])
def download():
    return send_file('image/received_image.jpg', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
