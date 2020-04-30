import requests
import json


# Função que grava o conteúdo retornado pela chamada à API no arquivo 'answer.json'
def write_json(archive_json):
	with open('request.json', 'w') as json_file:
		json.dump(json.loads(request.text), json_file, indent = 4)

# Token fornecido pela Codenation
token = '1158495dddc2bfea5532a710ce71e9b9d5932306'

# Faz uma chamada 'GET' à API passando o token como parâmetro.
request = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + token)

# Chama a função 'write_json' passando o arquivo obtido por request
write_json(request.text)

import decode
