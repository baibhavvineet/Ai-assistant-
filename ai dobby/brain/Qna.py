#open ai #api key
fileopen = open("data\\api.txt","r")
API = fileopen.read()
fileopen.close()

#importing
import openai
from dotenv import load_dotenv

#coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def QuestionsAns(question,chat_log = None):
    FileLog = open("database\\Qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 1,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {question} \nAnswer : {answer}"
    FileLog = open("database\\Qna_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer
