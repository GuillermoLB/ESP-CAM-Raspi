from flask import Flask, request
import boto3

access_key_id = 'AKIAVRJ2BC7EQV5SRNGP'
secret_access_key = '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'

client = boto3.client ('rekognition', region_name= 'us-west-2', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'imageFile' in request.files:
        image = request.files['imageFile']
        image.save('received_image.jpg')
        print('Image received')
    else:
        print('No image received')

    # Abre la imagen y lee su contenido en bytes
    with open('received_image.jpg', 'rb') as image:
        image_bytes = image.read()

    # Llama a la operación DetectLabels
    response = client.detect_labels(Image={'Bytes': image_bytes})

    # Imprime las etiquetas detectadas
    for label in response['Labels']:
        print(f"{label['Name']}: {label['Confidence']}")

    return '-----------'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)