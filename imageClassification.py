import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the pre-trained model
model = tf.keras.applications.MobileNetV2(include_top=True, weights='imagenet')

# Define a function to preprocess the image
def preprocess_image(image):
    # Convert the image to a NumPy array
    img_array = np.array(image)
    # Preprocess the image using the model's preprocessing function
    img_preprocessed = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    # Return the preprocessed image
    return img_preprocessed

# Define a function to classify the image
def classify_image(image):
    # Preprocess the image
    img_preprocessed = preprocess_image(image)
    # Expand the dimensions of the image to match the model's input shape
    img_expanded = np.expand_dims(img_preprocessed, axis=0)
    # Use the model to predict the top 5 most likely classes for the image
    predictions = model.predict(img_expanded)
    # Decode the predictions using the ImageNet class labels
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
    # Return the decoded predictions
    return decoded_predictions

# Load an example image
image_path = 'image.jpg'
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))

# Classify the image and print the top predictions
predictions = classify_image(image)
for i, prediction in enumerate(predictions[0]):
    print("{}. {}: {:.2f}%".format(i+1, prediction[1], prediction[2]*100))

# Show the image
plt.imshow(image)
plt.show()

