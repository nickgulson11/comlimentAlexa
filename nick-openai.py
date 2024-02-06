import requests

# OpenAI API Key
apiKey = "XXX"
url = "https://api.openai.com/v1/chat/completions"

# OpenAI Python Package Method - Alexa console refuses to dowload latest version
#import openai
#from openai import OpenAI
#client = OpenAI(api_key=apiKey)

def compliment(name):
    p = "Give a nice and witty two sentence compliment to my girlfriend " + name
    t = 0.7
    body = {
        "messages":[{"role": "user", "content": p}],
        "model":"gpt-3.5-turbo",
        "temperature": t,
        "max_tokens": 55
        }
    headers = {
                "Authorization": "Bearer "+apiKey,
                "Content-Type": "application/json"
               }
    response = requests.post(url, headers=headers, json=body).json()
    print(response)

    # OpenAI Python Package Method
    #response = client.chat.completions.create(
     #   messages=[{"role": "user", "content": p}],
      #  model="gpt-3.5-turbo",
       # temperature= t,
       # max_tokens = 55
    #)
    # compliment = response.choices[0].message.content
    # print(response)
    compliment = response['choices'][0]['message']['content']
    return compliment

print(compliment("emily"))