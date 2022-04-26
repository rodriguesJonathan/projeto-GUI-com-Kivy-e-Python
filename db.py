import json
def inserirNoBanco(dicionario):
	try:
		with open('dados.json', 'r') as json_file:                
			oldData = json.load(json_file)
		with open('dados.json', 'w') as json_file:
			oldData.append(dicionario)
			jsoned_data = json.dumps(oldData, indent=True)
			json_file.write(jsoned_data)
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		with open('dados.json', 'w') as json_file:
			jsoned_data = json.dumps([], indent=True)
			json_file.write(jsoned_data)
		inserirNoBanco(dicionario)
	

def lerTodoBancoDeDados():
	try:
		with open('dados.json', 'r') as json_file:                
			dicionario = json.load(json_file)
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		return {}
	else:
		return dicionario