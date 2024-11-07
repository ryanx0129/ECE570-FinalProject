from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch
import logging

# Initialize logging for fine-tuning
logging.basicConfig(level=logging.INFO, filename='fine_tuning.log', format='%(asctime)s - %(levelname)s - %(message)s')

class AdversarialDataset(torch.utils.data.Dataset):
    def __init__(self, examples, tokenizer, max_length=128):
        self.examples = examples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        example = self.examples[idx]
        inputs = self.tokenizer(
            example["input_text"], truncation=True, padding="max_length", max_length=self.max_length, return_tensors="pt"
        )
        labels = self.tokenizer(
            example["label"], truncation=True, padding="max_length", max_length=self.max_length, return_tensors="pt"
        ).input_ids
        inputs["labels"] = labels.squeeze()
        return {key: val.squeeze() for key, val in inputs.items()}

def fine_tune_model(model_name, adversarial_examples, output_dir="./fine_tuned_model"):
    logging.info(f"Fine-tuning model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    train_dataset = AdversarialDataset(adversarial_examples, tokenizer)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        logging_dir="./logs",
        save_steps=500,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    logging.info(f"Model fine-tuned and saved to {output_dir}")
