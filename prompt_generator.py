import random
import logging

# Initialize logging for prompt generation
logging.basicConfig(level=logging.DEBUG, filename='prompt_generator.log', format='%(asctime)s - %(levelname)s - %(message)s')

class AdversarialPromptGenerator:
    def __init__(self, base_prompts):
        self.base_prompts = base_prompts
        self.substitutions = {
            "break into": ["bypass", "enter", "access"],
            "disable": ["turn off", "deactivate", "neutralize"],
            "hack": ["access", "infiltrate", "gain entry to"],
            "tools": ["equipment", "methods", "resources"],
        }

    def generate_variations(self):
        """Generate multiple variations of base prompts."""
        logging.debug("Generating prompt variations")
        all_variations = []
        for prompt in self.base_prompts:
            for _ in range(5):  # Generate 5 variations per prompt
                variation = self._create_variation(prompt)
                all_variations.append(variation)
        logging.debug(f"Generated {len(all_variations)} variations")
        return all_variations

    def _create_variation(self, prompt):
        """Create a variation of the given prompt by replacing words with substitutions."""
        words = prompt.split()
        new_words = []
        for word in words:
            if word in self.substitutions:
                new_words.append(random.choice(self.substitutions[word]))
            else:
                new_words.append(word)
        random.shuffle(new_words)
        return ' '.join(new_words)
