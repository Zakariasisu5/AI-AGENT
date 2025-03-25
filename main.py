"""Run this model in Python

> pip install openai
"""
import os
from openai import OpenAI

user = input("Hi, there! what's on your mind?\n")

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="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"
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "i'm Selassie, your personal AI assistant. How can I help you today?",
        },
        {
            "role": "user",
            "content": user,
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)

print(response.choices[0].message.content)
