
# This code is complete using an API key. Please refer to the video after 10:04:00 - code with hurry

from openai import OpenAI
 # pip install OpenAI

# default to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="",  # you can write here your api key
)
 
completion = client.chat.completion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system","content": "you are virtual assistant, name jarvis skilled in general tasks like Alexa and Google cloud "},
    {"role": "user","content":"what is coding."}
  ]
)
print(completion.choices[0].message)