from transformers import pipeline
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "" 

def main():
    messages = [{ "content": "Hello, how are you?","role": "user"}]
    response = completion(model="gpt-3.5-turbo", messages=messages)
    print(response.choices[0].message.content)

    # query = {
    #     'question': 'What are my competitors doing that I should pay attention to?',
    #     'context': 
    #     """
    #     You are a senior data analyst and your job is to discover unique insights about competitors that can inform how my business should adapt its business strategies to stand out and become more competitive. Do not give me obvious insights, focus on uncovering hidden and implied strategies. Outline what the competitors strategies like are and then provide a recommendation for my company. Ask me what my company does and verify your assumptions with me before conducting your analysis.
    #     """
    # }
    
    # ques_to_text = pipeline("question-answering", model="deepset/tinyroberta-squad2")
    # answer = ques_to_text(query)['answer']
    # print('##############')
    # print(answer)
    # print('##############')

main()