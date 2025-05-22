import pathlib
import textwrap
import google.generativeai as genai
from dotenv import load_dotenv
import os

def main():

    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    print(f"API Key: {google_api_key}")

    genai.configure(api_key=google_api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    contador = 0

    while contador < 5:
        contador+=1
        pergunta = input('Faça a pergunta... ')
        response = chat.send_message(pergunta, stream=True)
        #print(response.text)

        for chunk in response:
         print(chunk.text)
         print("_"*80)


    print(chat.history)


if __name__ in "__main__":
    main()