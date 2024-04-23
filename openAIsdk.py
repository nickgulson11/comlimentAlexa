import openai
import json

# Load your API key from an environment variable or secret management service
openai.api_key = "XXX"

def compliment(name):
    p = "Give a nice compliment to my girlfriend " + name
    response = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=p, temperature=1, max_tokens=90)
    response = json.loads(str(response))
    compliment = response['choices'][0]['text']
    compliment = compliment[2:]
    return compliment

print(compliment("emily"))