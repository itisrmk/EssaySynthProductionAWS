from openai import OpenAI
import os

client = OpenAI(api_key='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')
def openai_response(school, major, check_essay_text, title):
    prompt = f'Improve the following essay: {check_essay_text} max 1000 words. Consider that my major is {major} and I am applying to {school}. The title is {title}.  Do not label any paragraphs. Do not write the ttile.Just give the text.'
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a collage essay writer."},
        {"role": "user", "content": prompt},
        ]
    )
    final_response =  response.choices[0].message.content
    # print(final_response)
    return final_response
