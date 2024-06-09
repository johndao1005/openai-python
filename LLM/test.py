import os
from transformers import AutoTokenizer, AutoModelForCausalLM,GPT2Tokenizer,GPT2LMHeadModel, pipeline
from spellchecker import SpellChecker
import string

# Set your Hugging Face API token
os.environ["HUGGINGFACE_TOKEN"] = "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"

# Load Llama
# tokenizer = AutoTokenizer.from_pretrained("../Llama")
# model = AutoModelForCausalLM.from_pretrained("../Llama")

# Load gpt2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Initialize grammar correction pipeline and spell checking library
corrector = pipeline('text-generation', model='gpt2')
spell = SpellChecker()

# Define command variations
command_variations = {
    "schedule a meeting": "create_appointment",
    "set up a meeting": "create_appointment",
    "arrange a meeting": "create_appointment",
    # Add more command variations here
}

# Get user input
user_input = input("You: ")

# Remove punctuation from user input
user_input = user_input.translate(str.maketrans('', '', string.punctuation))

# Correct spelling mistakes in user input
corrected_spelling_input = " ".join(spell.correction(word) for word in user_input.split())
corrected_grammar_input = corrector(corrected_spelling_input)[0]['generated_text']

# Encode input for GPT-2
encoded_input = tokenizer.encode_plus(corrected_grammar_input, return_tensors='pt')

# Get model output
output = model.generate(input_ids=encoded_input['input_ids'], 
                        attention_mask=encoded_input['attention_mask'], 
                        max_length=50, 
                        num_return_sequences=1, 
                        no_repeat_ngram_size=2)

# Decode output
output_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Check if output matches any command variation
for variation, command in command_variations.items():
    if variation in output_text:
        output_text = output_text.replace(variation, command)

# Print model response
print("Assistant: ", output_text)