import json
import hashlib


# Função que faz a escrita no arquivo passando o texto descriptografado.
def write_json(archive_json):
	with open('request.json', 'r') as json_file:
		decoded = json_file.readlines()
		decoded.append(str.replace(obj['decifrado'], '""','decrypted_phrases' ))

	with open('answer.json', 'w') as json_file:
		#json_file.writelines(decoded)
		json.dump(obj, json_file, indent = 4)

# Função que faz a descriptografia da frase passada por parâmetro.
def phrase_decryptor(encrypted_phrase):
	for letters in encrypted_phrase:
		decrypted = int(ord(letters))
		if letters == '.':
			phrase = chr(46)
		elif letters == ' ':
			phrase = chr(32)
		else:
			if (chr(decrypted - (obj['numero_casas'])) < chr(97)):
				phrase = chr(120)
			else:	
				phrase = chr(decrypted - (obj['numero_casas']))
		decrypted_phrase.append(phrase)

	return decrypted_phrase

# Faz a leitura do arquivo 'answer.json'
with open('request.json', 'r') as json_data:
	obj = json.load(json_data)

# Inicia uma lista com os caracteres para a descriptografia da frase
decrypted_phrase = []

# Indica o separador de caracteres da lista
separator = ''

# Informa que a frase a ser passada para a função 'phrase_decryptor' é a contida no atributo 'cifrado' do arquivo .json
encrypted_phrase = str(obj['cifrado'])

result = phrase_decryptor(encrypted_phrase)

decrypted_phrases = separator.join(result)

obj['decifrado'] = decrypted_phrases
write_json(obj['decifrado'])

# Criptografia(SHA1) da frase decodificada
summary_hash = hashlib.sha1()
summary_hash.update(obj['decifrado'].encode('utf-8'))

obj['resumo_criptografico'] = summary_hash.hexdigest()
write_json(obj['resumo_criptografico'])
