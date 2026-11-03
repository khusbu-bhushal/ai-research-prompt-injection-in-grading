#this file sends sends message to mistral model and prints what it says back to test to see if this setup will work

import ollama

response = ollama.chat(
    model="mistral:v0.2",  #model pulls the exact tag
    messages=[{"role": "user", "content": "Say hello in one sentence."}],  #messages is the conversation
    options={"temperature": 0, "seed": 42},    #settings used for grading
)
print(response["message"]["content"])
