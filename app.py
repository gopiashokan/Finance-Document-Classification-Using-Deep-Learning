import os
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.add_vertical_space import add_vertical_space
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from warnings import filterwarnings
filterwarnings('ignore')


def streamlit_config():

    # page configuration
    st.set_page_config(page_title='Document Classification', layout='centered')

    # page header transparent color
    page_background_color = """
    <style>

    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }

    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
    st.markdown(f'<h1 style="text-align: center;">Financial Document Classification</h1>',
                unsafe_allow_html=True)
    add_vertical_space(2)


def display_html_document(input_file):

    # Read the file content
    html_content = input_file.getvalue().decode("utf-8")

    # Define CSS to control the container size and center content
    styled_html = f"""
    <div style="width: 610px; height: 300px; 
                overflow: auto; border: 1px solid #ddd; 
                padding: 10px; background-color: white; 
                color: black; white-space: normal; 
                display: block;">
        {html_content}
    </div>
    """

    # Display the HTML content inside a fixed-size container
    components.html(styled_html, height=320, width=650, scrolling=False)


def text_extract_from_html(html_file):

    # Read the uploaded HTML file
    html_content = html_file.read().decode('utf-8')

    # Parse the HTML Content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the Text
    text = soup.get_text()

    # Split the Text and Remove Unwanted Space
    result = [i.strip() for i in text.split()]
    result = ' '.join(result)

    return result


def classify_text_with_huggingface_api(extracted_text):
     
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the Hugging Face API token from environment variables
    hf_token = os.getenv("HUGGINGFACE_TOKEN")

    # Define the Hugging Face API URL for the model
    API_URL = "https://api-inference.huggingface.co/models/gopiashokan/Financial-Document-Classification-using-Deep-Learning"

    # Set the authorization headers with the Hugging Face token
    HEADERS = {"Authorization": f"Bearer {hf_token}"}

    # Send a POST request to the Hugging Face API with the extracted text
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": extracted_text})
    
    # Parse and return the JSON response
    if response.status_code == 200:
        result = response.json()
        return result[0]
    
    else:
        return None

    
def prediction(input_file):

    # Extract text from the uploaded HTML file  
    extracted_text = text_extract_from_html(input_file)

    # Limit the extracted text to the first 512 characters to avoid API input limits  
    extracted_text = extracted_text[0:512]

    # Classify the extracted text using the Hugging Face API  
    result = classify_text_with_huggingface_api(extracted_text)

    if result is not None:
        # Select the prediction with the highest confidence score  
        prediction = max(result, key=lambda x: x['score'])

        # Map model labels to human-readable class names 
        label_mapping = {'LABEL_0':'Others', 'LABEL_1':'Balance Sheets', 'LABEL_2':'Notes', 'LABEL_3':'Cash Flow', 'LABEL_4':'Income Statement'}

        # Get the predicted class name based on the model output  
        predicted_class = label_mapping[prediction['label']]

        # Convert the confidence score to a percentage  
        confidence = prediction['score'] * 100

        # Display the prediction results
        add_vertical_space(1)
        st.markdown(f"""
            <div style="text-align: center; line-height: 1; padding: 0px;">
                <h4 style="color: orange; margin: 0px; padding: 0px;">{confidence:.2f}% Match Found</h4>
                <h3 style="color: green; margin-top: 10px; padding: 0px;">Predicted Class = {predicted_class}</h3>
            </div>
        """, unsafe_allow_html=True)


    else:
        add_vertical_space(1)
        st.markdown(f'<h4 style="text-align: center; color: orange; margin-top: 10px;">Refresh the Page and Try Again</h4>', 
                        unsafe_allow_html=True)



# Streamlit Configuration Setup
streamlit_config()
    

try:

    # File uploader to upload the HTML file
    input_file = st.file_uploader('Upload an HTML file', type='html')

    if input_file is not None:
        
        # Display the HTML Document to User Interface
        display_html_document(input_file)
        
        # Predict the Class and Confidence Score
        with st.spinner('Processing'):
            prediction(input_file)


except Exception as e:
    st.markdown(f'<h3 style="text-align: center;">{e}</h3>', unsafe_allow_html=True)
