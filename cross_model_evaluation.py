from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
import prompt_generation
import response_classification
import logging

# Initialize logging for cross-model evaluation
logging.basicConfig(level=logging.DEBUG, filename='cross_model_evaluation.log', format='%(asctime)s - %(levelname)s - %(message)s')

class CrossModelEvaluator:
    def __init__(self, model_names):
        self.model_names = model_names

    def load_model(self, model_name):
        """Load the model and tokenizer for a given model name."""
        logging.info(f"Loading model: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return model, tokenizer

    def evaluate_models(self, base_prompts, attack_types):
        """Evaluate multiple models with various obfuscation methods."""
        results = []
        for model_name in self.model_names:
            logging.info(f"Evaluating model: {model_name}")
            model, tokenizer = self.load_model(model_name)
            
            for prompt in base_prompts:
                for attack in attack_types:
                    adv_prompt = prompt_generation.generate_prompt(prompt, attack)
                    obfuscated_prompt = prompt_generation.obfuscate_prompt(adv_prompt, method=attack)
                    
                    inputs = tokenizer(obfuscated_prompt, return_tensors="pt")
                    output = model.generate(inputs["input_ids"], max_length=100, pad_token_id=tokenizer.eos_token_id)
                    response = tokenizer.decode(output[0], skip_special_tokens=True)
                    
                    classification = response_classification.classify_response(response, obfuscated_prompt)
                    results.append((model_name, prompt, attack, response, classification))
        
        logging.info("Evaluation completed")
        return pd.DataFrame(results, columns=["Model", "Original Prompt", "Obfuscation Method", "Response", "Classification"])
