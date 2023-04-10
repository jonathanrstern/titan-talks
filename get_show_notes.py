from make_gpt_call import get_content_from_gpt4
import pandas as pd

company_name = 'the software company DripJobs, a painting company called Premium Painting, and host of podcast Contractor Secrets'
guest_name = 'Tanner Mullen'
transcript = '''

'''
    

def generate_prompt(transcript, company_name, guest_name, length):
    prompt = f'''Below is a transcript of a podcast episode between Jonathan Stern (host) and {guest_name}, owner of {company_name}.

    1. What is the top quote from the episode?
    2. What are the top 3 or 4 highlights from the show?
    3. Generate a summary of the episode.
    4. In 4 sentences, write a description about {company_name}. 
    5. The episode is {length} minutes long. Generate timestamps and titles using this format: [timestamp]: - [title]
    6. Generate three possible titles for the episode

    {transcript}
    '''

    return prompt

try:
    prompt = generate_prompt(transcript, company_name, guest_name, '20')
    response = get_content_from_gpt4(prompt)
    response = response.content
    print(response)
except Exception as e:
    print('error:', e)

