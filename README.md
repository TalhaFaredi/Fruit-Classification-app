# Fruit Classification App with Streamlit

This is a simple Streamlit app for classifying fruits using a pre-trained deep learning model. Users can upload an image, and the app will make predictions based on a provided list of fruit classes.

## Getting Started

### Prerequisites

Make sure you have the required Python packages installed:

- Streamlit
- Pillow
- Keras
- TensorFlow

### Running the App

To run the Streamlit app, use the following command:

```streamlit run app.py```

This will open a new tab in your web browser with the Fruit Classification App.

### Usage

1. Upload an image using the "Choose an image..." button.
2. Click the "Predict" button to see the predicted fruit.

## Model and Classes

The deep learning model was pre-trained on a dataset of 10 fruit classes. The class labels include:

- Apple
- Avocado
- Banana
- Cherry
- Kiwi
- Mango
- Orange
- Pineapple
- Strawberries
- Watermelon

## File Structure

- **app.py**: Main Streamlit app script.
- **your_model.h5**: Pre-trained model file (replace with the actual model file).
- **README.md**: Project documentation.

## Acknowledgments

- The model was trained using Keras and TensorFlow.
- Streamlit is a great tool for creating interactive web applications with minimal effort.

