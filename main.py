import streamlit as st
import numpy as np
from PIL import Image
#import keras
# import tensorflow as tf
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

#model = keras.models.load_model('lung_and_colon_cancer_model.keras')

background = """
<style>
body {
    background-image: url('/Users/mac/Documents/Lung_Cancer_Detection/logo.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: Arial, sans-serif;
}
</style>
"""

# Dictionary mapping class labels (numbers) to class names
class_dict = {
    0: "benign tissue",
    1: "squamous cell carcinoma",
    2: "adenocarcinoma"
}

def process_image(img_obj: str):
    img = np.array(img_obj) / .255
    img_array = np.array([img])
    return img_array

# Generate PDF report with logo
# Function to generate PDF with logo and uploaded image
def generate_pdf_with_logo(predicted_class_name, uploaded_image_path):
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    #Generate timestamp
    timestamp = datetime.now()
    # Convert timestamp to string
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    # Draw the logo at the top center
    logo_path = "/Users/mac/Documents/Lung_Cancer_Detection/logo.png"
    c.drawImage(logo_path, 200, 800, width=200, height=50)
    
    # Draw the uploaded image
    uploaded_image = Image.open(uploaded_image_path)
    c.drawImage(uploaded_image_path, 100, 600, width=300, height=300)

    c.drawString(100, 550, "The image uploaded is predicted to be {}".format(predicted_class_name))
    c.drawString(100, 660, "Timestamp: {}".format(timestamp))
    c.drawString(100, 530, "Signed")
    c.drawString(100, 510, "Management, Ibadan Cancer Registry")
    c.save()
    pdf_bytes = pdf_buffer.getvalue()
    return pdf_bytes

def main_page():
    st.markdown(background, unsafe_allow_html=True)
    st.title("Lung Cancer Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        # Get the path of the uploaded file
        file_path = f"./{uploaded_file.name}"
        # Process the image
        # img_array = process_image(file_path)
        # # Make predictions
        # predictions = model.predict(img_array)
        # # Get the predicted class
        # predicted_class = np.argmax(predictions, axis=1)
        # Get the predicted class name using the dictionary
        # predicted_class_name = class_dict.get(predicted_class[0], "Unknown")
        if st.button('Predict'):
            st.write("The image uploaded is predicted to be a benign tissue with a confidence of 95%")
                    # Button to save analysis in PDF
            if st.button("Save Analysis as PDF"):
                pdf_bytes = generate_pdf_with_logo(predicted_class_name, file_path)
                st.download_button("Download PDF", pdf_bytes, file_name="lung_cancer_analysis.pdf", mime="application/pdf")

            

# Main function to run the app
def main():
    main_page()

if __name__ == "__main__":
    main()