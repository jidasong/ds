import os
import requests

API_URL = "https://api.deepseek.com/v1/example"  # Replace with the actual endpoint
API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not API_KEY:
    raise RuntimeError("Set the DEEPSEEK_API_KEY environment variable.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "prompt": "Hello from DeepSeek!",
    # Add additional parameters required by the DeepSeek API here
}

response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
response.raise_for_status()

print(response.json())
