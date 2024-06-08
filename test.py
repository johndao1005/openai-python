from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Get user input
user_input = input("You: ")

# Encode input for GPT-2
input_ids = tokenizer.encode(user_input, return_tensors='pt')

# Get model output
output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

# Decode output
output_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

# Print model response
print("Assistant: ", output_text)

# TODO: Parse response for commands and execute them