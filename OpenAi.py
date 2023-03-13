import openai
import os
import requests

# Set OpenAI API key
openai.api_key = "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"

# Set up API endpoint URL and parameters
url = "https://api.openai.com/v1/engines/davinci-codex/completions"
params = {
    "prompt": "",
    "temperature": 0.7,
    "max_tokens": 60,
    "n": 1,
    "stop": "\n"
}

# Read in text from file
filename = "predicted_letters.txt"
with open(filename, "r") as f:
    input_text = f.read()

# Set prompt to input text
params["prompt"] = input_text

# Send POST request to OpenAI API
response = requests.post(url, headers={"Authorization": f"Bearer {openai.api_key}"}, json=params)

# Extract generated text from response
generated_text = response.json()["choices"][0]["text"]

# Print generated text
print(generated_text)
