import os
import openai
openai.api_key=""

messages_parsed= [
    {"role": "system" ,
     "content": "Please provide the brief history about character in french"},
    {"role":"user",
     "content":"Who is Iron man ?"} ]
def get_completion_from_messages(
        messages,
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=500):

    response= openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens)

    return response.choices[0].message["content"]

print(get_completion_from_messages(messages_parsed))

