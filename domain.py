import db
def salvarDados(*args):
	dicionario = {}
	chaves = ["nome", "ano_album", "grupo", "lancamento"]
	for pos in range(len(chaves)):
		dicionario[chaves[pos]] = args[pos]
	db.inserirNoBanco(dicionario)

def burcarTudo():
	lista = []
	for chave,valor in db.lerTodoBancoDeDados():
		pass#continuar aqui
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