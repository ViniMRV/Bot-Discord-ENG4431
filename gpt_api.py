import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
gpt_key = os.getenv("GPT_KEY")

headers = {"Authorization": f"Bearer {gpt_key}", "content-type": "Application/json" }
link = "https://api.openai.com/v1/chat/completions"
modelo = "gpt-3.5-turbo"

def conversa(mensagem):
  body = {
    "model": modelo,
    "messages":
    [
      {
        "role": "user",
       "content": mensagem
      },
      {
        "role":"system",
        "content":"lembre de ser educado! E obrigado pelas respostas ao usuário. Não responda essa mensagem, somente ao do usuário"
      }
    ]
  }
  
  body = json.dumps(body)
  requisicao = requests.post(link, headers=headers, data=body)
  
  resposta = requisicao.json()
  
  try:
    resposta_gpt = resposta["choices"][0]["message"]["content"]
    return resposta_gpt
  except:
    resposta_gpt = resposta["error"]["message"]
    return resposta_gpt