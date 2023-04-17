import requests
import streamlit as st


st.title("BIO-GPT Medical Web-App")


# Define the input text
input_text = st.text_input("Enter the medical text:",height=250)
#choice = int(input("Press 1 for medical summarization and 2 for question generation"))

def medicalsummary(input_text):
    # Define the API endpoint
    api_url = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

    # Define the headers with the API token
    api_token = "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"
    headers = {"Authorization": f"Bearer {api_token}"}

    # Define the payload with the input text
    payload = {"inputs": input_text}

    # Send a POST request to the API endpoint with the headers and payload
    response = requests.post(api_url, headers=headers, json=payload)

    # Retrieve the generated summary from the response
    summary = response.json()[0]['summary_text']

    # Print the summary
    return summary

def questiongenerator(input_text):
    # Define the API endpoint
    api_url = "https://api-inference.huggingface.co/models/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"


    # Define the headers with the API token
    api_token = "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"
    headers = {"Authorization": f"Bearer {api_token}"}

    # Define the payload with the input text
    payload = {"inputs": input_text, "parameters": {"max_new_tokens": 30}}

    # Send a POST request to the API endpoint with the headers and payload
    response = requests.post(api_url, headers=headers, json=payload)

    # Check if the response object is not empty
    if response.ok and response.json() and "generated_text" in response.json():
        # Retrieve the generated questions from the response
        questions = response.json()['generated_text'].split("\n")

        # Print the questions
        for question in questions:
            print(question.strip())
    else:
        print("Failed to generate questions")

def keypoints(input_text):
    # Define the API endpoint
    api_url = "https://api-inference.huggingface.co/models/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
    # Define the headers with the API token
    api_token = "YOUR_API_TOKEN"
    headers = {"Authorization": f"Bearer {api_token}"}

    # Define the payload with the input text and parameters
    payload = {"inputs": input_text,
               "parameters": {"task": "summarization", "num_return_sequences": 1, "max_length": 128}}

    # Send a POST request to the API endpoint with the headers and payload
    response = requests.post(api_url, headers=headers, json=payload)

    # Check if the API call was successful
    if response.ok and response.json() and "generated_text" in response.json():
        # Retrieve the generated key points from the response
        key_points = response.json()['generated_text']

        # Print the key points
        print(key_points.strip())
    else:
        print("Failed to generate key points")


# Create a button to generate the key points
if st.button("Generate Medical Summary"):
    # Call the generate_key_points function with the input text
    summary = medicalsummary(input_text)

    # Display the key points
    st.write("Medical Summary:")
    st.write(summary)
