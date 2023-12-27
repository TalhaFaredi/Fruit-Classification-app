import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np

# Load the pre-trained model
model = load_model('path.h5')  # Replace with the actual path to your model file

# Define class labels
class_labels = ['apple', 'avocado', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'pineapple', 'strawberries', 'watermelon']

def preprocess_image(img):
    img = img.resize((150, 150)) 
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Streamlit app
st.title('Fruit Classification App')
st.write('You can predict: apple, avocado, banana, cherry, kiwi, mango, orange, pineapple, strawberries, watermelon')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    if st.button('Predict'):
        uploaded_image = Image.open(uploaded_file)
        processed_image = preprocess_image(uploaded_image)

        predictions = model.predict(processed_image)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]

        st.success(f'Predicted fruit: {predicted_class_label}')
