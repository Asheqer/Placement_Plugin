import openai
import json
from plugin_queries import QUERIES_INPUT

GPT_MODEL = "gpt-3.5-turbo"
openai.api_key = "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"

def json_config(query,input):
    completion = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": "Output only valid JSON"},
            {"role": "user", "content": query},
        ],
        temperature=0.5,
    )

    text = completion.choices[0].message.content
    parsed = json.loads(text)

    return parsed
USER_QUESTION = input("Request: ")
print(json_config(QUERIES_INPUT,USER_QUESTION))