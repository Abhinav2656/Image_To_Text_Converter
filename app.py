import os
import time
from typing import Any
import requests
import streamlit as st
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

# Retrieve API keys from the environment variables
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Function to display a progress bar
def progress_bar(amount_of_time: int) -> None:
    progress_text = "Please wait, Generative models are hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1) 
    my_bar.empty()

# Function to generate a brief description from an image using Hugging Face pipeline
def generate_text_from_image(url: str) -> str:
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    generated_text = image_to_text(url)[0]["generated_text"]
    print(f"IMAGE INPUT: {url}")
    print(f"GENERATED TEXT OUTPUT: {generated_text}")
    return generated_text

# New function to generate a more **detailed description** of the image
def generate_detailed_description(url: str) -> str:
    # Using the same pipeline with a different prompt, or adjusting the model if needed
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    detailed_description = image_to_text(url)[0]["generated_text"]
    print(f"DETAILED DESCRIPTION OUTPUT: {detailed_description}")
    return detailed_description

# Function to generate a story using Cohere's LLM, now with detailed description
def generate_story_from_image(scenario: str, detailed_description: str) -> str:
    prompt = f"""
    You are a talented storyteller who can create a story from a detailed scenario and description.
    Create a story using the following scenario. The story should be rich, imaginative, and a maximum of 100 words long.

    CONTEXT: {scenario}
    DETAILED DESCRIPTION: {detailed_description}
    
    STORY:
    """
    # Call Cohere API to generate the story
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "command-xlarge-nightly",  # Cohere's model
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.9,
        "stop_sequences": ["\n"]
    }
    
    response = requests.post("https://api.cohere.ai/v1/generate", headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        if "generations" in response_json and len(response_json["generations"]) > 0:
            generated_story = response_json["generations"][0]["text"]
            return generated_story.strip()
        else:
            return "Error: No story generated. Please try again."
    else:
        return f"Error: Failed to generate story. API returned status code {response.status_code}: {response.text}"

# Main application logic
def main() -> None:
    st.set_page_config(page_title="Image to Story Converter", page_icon="🖼️")

    st.title("🖼️ Image-to-Story Converter")
    st.markdown("Upload an image to generate a story and speech output!")

    uploaded_file = st.file_uploader("Choose an image", type="jpg")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        progress_bar(100)

        with open(uploaded_file.name, "wb") as file:
            file.write(uploaded_file.getvalue())

        # Generating brief text (scenario) from the image
        scenario = generate_text_from_image(uploaded_file.name)

        # Generating a detailed description of the image
        detailed_description = generate_detailed_description(uploaded_file.name)

        # Generating a story using both the scenario and detailed description
        story = generate_story_from_image(scenario, detailed_description)

        st.subheader("Generated Scenario")
        st.write(scenario)

        st.subheader("Detailed Description")
        st.write(detailed_description)

        st.subheader("Generated Story")
        st.write(story)

if __name__ == "__main__":
    main()
