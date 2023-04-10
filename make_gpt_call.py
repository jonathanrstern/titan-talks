import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

text_davinci_002 = "https://api.openai.com/v1/engines/text-davinci-002/completions"
text_davinci_003 = "https://api.openai.com/v1/engines/text-davinci-003/completions"

def make_gpt3_call(body, model):
    if model == 'text_davinci_002':
        url = text_davinci_002
    elif model == 'text_davinci_003':
        url = text_davinci_003

    headers = {"Authorization": "Bearer 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"}
    response = requests.post(url=url, headers=headers, json=body)
    return response

def get_content_from_gpt3(prompt, max_tokens, temperature, model):
    counter = 0
    error = True
    while error == True and counter < 5:
        try:
            counter += 1
            body = {"prompt": prompt, "temperature": temperature, "max_tokens": max_tokens, "top_p": 1.0, "frequency_penalty": 0, "presence_penalty": 0.0}
            gpt3_response = make_gpt3_call(body, model).json()
            print('gpt3_response',gpt3_response)
            gpt_choices = gpt3_response["choices"]
            if len(gpt_choices):
                first_choice_text = gpt_choices[0]["text"]
                error = False
                return first_choice_text
            raise Exception("No GPT3 Choices Present")
        except Exception as e:
            print('error getting gpt-3 content:', e)
    print('tried and failed 5 times')
    return ""

def get_content_from_gpt4(content):
    counter = 0
    error = True
    while error == True and counter < 5:
        try:
            gpt4_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"{content}"}]
            )
            gpt_choices = gpt4_response.choices
            if len(gpt_choices):
                message = gpt4_response.choices[0].message
                error = False
                return message
            raise Exception("No GPT3 Choices Present")
        except Exception as e:
            print('error getting gpt-3 content:', e)
    print('tried and failed 5 times')
    return ""


