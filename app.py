import requests
import streamlit as st
import json

st.set_page_config(layout="wide",page_title="BioGPT Clinical Webapp")

st.title("BIO-GPT Medical Web-App")

# Define the API endpoint
api_url = "https://api-inference.huggingface.co/models/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"


# Define the headers with the API token
api_token = "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"
headers = {"Authorization": f"Bearer {api_token}"}
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

def keypoints(input_text):
    # Define the API endpoint
    #api_url = "https://api-inference.huggingface.co/models/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
    # define the API endpoint
    endpoint = "https://api-inference.huggingface.co/models/dmis-lab/biobert-base-cased-v1.1"


    # Define the headers with the API token
    #api_token = "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"
    #headers = {"Authorization": f"Bearer {api_token}"}
    
    # define the headers and payload for the API request
    headers = {"Authorization": "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", "Content-Type": "application/json"}
    payload = {"inputs": input_text}
    
    # Define the payload with the input text
    #payload = {"inputs": input_text, "parameters": {"max_new_tokens": 30}}

    # Send a POST request to the API endpoint with the headers and payload
    #response = requests.post(api_url, headers=headers, json=payload)

    # Check if the response object is not empty
    #if response.ok and response.json() and "generated_text" in response.json():
        # Retrieve the generated questions from the response
        #questions = response.json()['generated_text'].split("\n")

        # Print the questions
        #for question in questions:
            #print(question.strip())
    #else:
        #print("Failed to generate questions")
       # make the API request and decode the response
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    output = json.loads(response.content.decode("utf-8"))["outputs"][0]
    return output

# Define a function to perform entity recognition
def extract_entities(input_text):
    
    

    
    # Define the payload with the input text and parameters
    payload = {"inputs": input_text, "parameters": {"task": "ner"}}

    # Send a POST request to the API endpoint with the headers and payload
    response = requests.post(api_url, headers=headers, json=payload)

    # Check if the API call was successful
    if response.ok and response.json() and "predictions" in response.json():
        # Retrieve the entities from the response
        entities = response.json()["predictions"][0]["entity_group"]
        entity_text = response.json()["predictions"][0]["entity"]

        # Return the entities and their corresponding text
        return entities, entity_text
    else:
        return [], []
    
# Define the input text
input_text = st.text_area(label="Enter the medical text:", height=250)

# Create a button to generate the key points
if st.button("Generate Medical Summary"):
    # Call the generate_key_points function with the input text
    summary = medicalsummary(input_text)

    # Display the key points
    st.write("Medical Summary:")
    st.write(summary)
    
if st.button("Generate Medical Key Points"):
    # Call the generate_key_points function with the input text
    key_points = keypoints(input_text)

    # Display the key points
    st.write("Medical Key Points:")
    st.write(key_points)


# Create a button to perform entity recognition
if st.button("Extract Entities"):
    # Call the extract_entities function with the input text
    entities, entity_text = extract_entities(input_text)

    # Display the extracted entities
    
    st.write("Entities found:")
    for i in range(len(entities)):
       st.write(f"{entities[i]}: {entity_text[i]}")
    
