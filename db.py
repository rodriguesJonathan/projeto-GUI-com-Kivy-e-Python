import json
def inserirNoBanco(*args):
	try:
		dicionario = {}
		chaves = ["nome", "ano_album", "grupo", "lancamento"]
		for pos in range(len(chaves)):
			dicionario[chaves[pos]] = args[pos]
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
		inserirNoBanco(*args)
	

def lerTodoBancoDeDados():
	lista = []
	try:
		arquivo = open("db.txt", 'r')
		linhas = arquivo.readlines()
		arquivo.close()
		num = 1
		for linha in linhas:
			lista.append(linha.strip().split(";"))
			num += 1
	finally:
		return lista

def buscarPorNomeArtistaBanda(nome):
	nome = nome.lower()
	lista = []
	arquivo = open("db.txt", 'r')
	linhas = arquivo.readlines()
	arquivo.close()
	num = 1
	for linha in linhas:
		linha = linha.strip().split(";")
		if nome in linha[2]:
			lista.append([num] + linha)
			num += 1
	return lista

def buscarPorAnoBanda(anoEscolhido, condicao):
	ANTERIOR = 1
	IGUAL = 2
	POSTERIOR = 3

	lista = []
	arquivo = open("db.txt", 'r')
	linhas = arquivo.readlines()
	arquivo.close()

	num = 1
	if condicao == ANTERIOR:
		for linha in linhas:
			linha = linha.strip().split(";")
			anoAlbum = int(linha[1])
			if anoAlbum <= anoEscolhido:
				lista.append([num]+linha)
				num+=1
	elif condicao == IGUAL:
		for linha in linhas:
			linha = linha.strip().split(";")
			anoAlbum = int(linha[1])
			if anoAlbum == anoEscolhido:
				lista.append([num]+linha)
				num+=1
	elif condicao == POSTERIOR:
		for linha in linhas:
			linha = linha.strip().split(";")
			anoAlbum = int(linha[1])
			if anoAlbum >= anoEscolhido:
				lista.append([num]+linha)
				num+=1
	return lista