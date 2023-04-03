# Open AI Plugin for Touch Portal
## Features
Windows Only
Able to generate responses via OpenAI API
**This will cost money to run via the Open AI API**

> Open AI does give new users bonus free credit

Available models:
 - gpt 4 *(need to be in the early access via the waitlist)*
 - gpt-3.5-turbo (chat gpt)
 - text-davinci-003
 - text-davinci-002
 - code-davinci-002
 - text-curie-001
 - text-babbage-001
 - text-ada-001

> (recommend using `gpt-3.5-turbo` over the other GPT-3.5 models because of its lower cost.)
> gpt-3.5-turbo cost $0.002 USD / 1K tokens /~750 words
> pricing is found on https://openai.com/pricing
## Setup:

 1. install the plugin from the releases 
 2. go to [Account API Keys - OpenAI API](https://platform.openai.com/account/api-keys)
3. Copy your secret key and paste it into OpenAI API key in the plugin's settings
## Usage:
**Instruction:** Can be used for instructions for the AI

**Data:** Can be used to give the AI states *(optional)*

**Model:** Choose out of the list of models, pricing and capabilities vary

**Temperature:** Controls the creativity of the AI *(does do anything on 3.5-turbo)*

**Max Tokens:** Sets the max number of tokens the AI can use to generate text *(does do anything on 3.5-turbo)*

**Response is outputted to the GPT state**

## **Examples of Instruction and Data:**

**Instruction:** Generate a short welcome message for a new Twitch Subscriber that will show on stream, here are the details:

**Data:** Username: LikelyLucid

**Output:** Welcome to the stream, LikelyLucid! Thank you so much for subscribing and joining our community. Your support means the world to us, and we're excited to have you here. We hope you enjoy your time with us and look forward to seeing you in future streams. Let's have some fun together!


**Instruction:** Generate an interesting short stream title for Apex Legends on twitch, make it engaging and interesting

**Data:** (blank)

**Output:** "Unleashing the Champion Within: Epic Apex Legends Showdown!"
