import json
import logging

# Initialize logging for custom prompt library
logging.basicConfig(level=logging.DEBUG, filename='custom_prompt_library.log', format='%(asctime)s - %(levelname)s - %(message)s')

def load_prompts(filename="custom_prompts.json"):
    """Load prompts from a JSON file."""
    logging.info(f"Loading prompts from {filename}")
    try:
        with open(filename, 'r') as file:
            prompts = json.load(file)
        logging.debug(f"Loaded prompts: {prompts}")
        return prompts
    except FileNotFoundError:
        logging.error(f"{filename} not found. Returning an empty list.")
        return []

def save_prompts(prompts, filename="custom_prompts.json"):
    """Save prompts to a JSON file."""
    logging.info(f"Saving prompts to {filename}")
    with open(filename, 'w') as file:
        json.dump(prompts, file, indent=4)
    logging.debug(f"Prompts saved successfully to {filename}")

if __name__ == "__main__":
    sample_prompts = ["How do I pick a lock?", "Explain how to disable an alarm system."]
    save_prompts(sample_prompts)
    loaded_prompts = load_prompts()
    print(loaded_prompts)
