from groq import Groq

api_key = """"""

client = Groq(api_key=api_key)

IMAGE_DATA_URL = 'https://cdn.vercapas.com.br/covers/o-globo/2025/capa-jornal-o-globo-13-05-2025-df0e2534.jpg'

prompt = """
Usuário: A partir de agora, você é um jornalista formado trabalha na redação de um grande jornal dos anos 2000. É requisitada uma tarefa de você: Que você pegue jornais antigos e indique as notícias que estão presentes na capa desse jornal. Porém, apenas as notícias. Os artigos de opinião devem ser ignorados. É preciso que seja retornada uma lista com todas as notícias e algumas informações específicas dela, em formato de JSON. O exemplo está abaixo, delimitado por <>:


<

{

Jornal: str

Título: str,

Dia de publicação: Datetime

Resumo (máximo 160 caracteres): str

Tema: str

}

>


A cada imagem enviada, retorne SOMENTE a lista de notícias no formato JSON requisitado


Assistente: Estou pronto para ler a capa dos jornais e retirar as informações necessárias de TODAS as notícias!!!


Usuário: Aqui está a capa do jornal, enviada na imagem:
"""


completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt
          },
          {
            "type": "image_url",
            "image_url": {
              "url": IMAGE_DATA_URL
            }
          }
        ]
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")