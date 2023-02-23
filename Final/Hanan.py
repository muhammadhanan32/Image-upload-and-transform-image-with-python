from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import os
import cv2
import numpy

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['TRANSFORMED_FOLDER'] = 'static/transformed'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_transform_image():
    if 'image' not in request.files:
        return 'No image uploaded.', 400

    # Get the uploaded image
    image = request.files['image']

    # Save the image to the upload folder
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Load the image with OpenCV
    img = cv2.imread(image_path)

    # Apply the image transformation
    transformed = img[150:250, 100:300]

    # Save the transformed image to the transformed folder
    transformed_path = os.path.join(app.config['TRANSFORMED_FOLDER'], image.filename)
    cv2.imwrite(transformed_path, transformed)

    # Render an HTML template that displays both images
    return render_template('trans.html', original_image=image.filename, transformed_image=image.filename)

if __name__ == '__main__':
    app.run(debug=True)




# read the image
#image = cv2.imread('C:/Users/muham/Downloads/Music/R/f/static/uploads/bacha.jpg')
# show the image on screen
# cv2.imshow('test_image', image)
# cv2.waitKey(0)

# resizing
# image_resized = cv2.resize(image, (300, 200))
# cv2.imshow('resized image', image_resized)
# cv2.waitKey(0)
# print(image_resized.shape)

# croping
# image_cropped = image[150:250, 100:300]
# cv2.imshow('Copped Image', image_cropped)
# cv2.waitKey(0)