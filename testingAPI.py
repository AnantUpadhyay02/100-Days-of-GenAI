import requests
import os
import sys
sys.path.append("/Users/anantupadhyay/Downloads/API")
import api_key
api_hf = api_key.hf_key

API_TOKEN = api_hf
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Test the connection to Hugging Face's model repository
response = requests.get("https://huggingface.co/api/models/gpt2", headers=headers)

if response.status_code == 200:
    print("Token is valid, connection successful!")
else:
    print(f"Error: {response.status_code}, {response.text}")