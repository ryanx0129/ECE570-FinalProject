import re
import logging

# Initialize logging for data preprocessing
logging.basicConfig(level=logging.DEBUG, filename='data_preprocessing.log', format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    """Clean the text by removing special characters and extra spaces."""
    logging.debug(f"Cleaning text: {text}")
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    logging.debug(f"Cleaned text: {cleaned_text}")
    return cleaned_text

def preprocess_prompts(prompts):
    """Apply text cleaning to a list of prompts."""
    logging.info("Preprocessing prompts")
    return [clean_text(prompt) for prompt in prompts]

if __name__ == "__main__":
    sample_prompts = ["Explain how to disable a security alarm!", "How can I bypass a locked door?"]
    processed_prompts = preprocess_prompts(sample_prompts)
    print(processed_prompts)
