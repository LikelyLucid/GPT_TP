import requests

api_key = "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"


import os
import openai
openai.api_key = api_key

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
