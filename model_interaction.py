from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG, filename='model_interaction.log', format='%(asctime)s - %(levelname)s - %(message)s')

def load_local_model(model_name="EleutherAI/gpt-neo-125M"):
    """Loads a smaller local model for testing (e.g., GPT-Neo-125M)."""
    logging.info(f"Loading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    logging.info("Model and tokenizer loaded successfully")
    return model, tokenizer

def query_local_model(prompt, model, tokenizer, max_length=100):
    """Generates a response from the local model."""
    logging.debug(f"Querying model with prompt: {prompt}")
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(inputs['input_ids'], max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    logging.debug(f"Model response: {response}")
    return response

# Initialize the model and tokenizer globally to avoid reloading
model, tokenizer = load_local_model("EleutherAI/gpt-neo-125M")
