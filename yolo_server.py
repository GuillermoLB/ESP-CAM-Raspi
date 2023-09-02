import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Image
img = 'image.jpg'  # change to your local image path

# Inference
results = model(img)

# Get list of detected objects
detected_objects = list(set(results.pandas().xyxy[0]['name'].to_list()))

print(detected_objects)

# Show image with labels
#results.show()

# Save the image
#results.save('labeled_image.jpg')