from openai import OpenAI
import json

# Load your API key from an environment variable or secret management service
apiKey = "XXX"
client = OpenAI(api_key=apiKey)

def compliment(name):
    p = "Give a nice and witty two sentence compliment to my girlfriend " + name
    t = 0.7
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": p}],
        model="gpt-3.5-turbo",
        temperature= t,
        max_tokens = 55
    )
    # print(response)
    compliment = response.choices[0].message.content
    return compliment

print(compliment("emily"))