def inserirNoBanco(*args):
	file = open("db.txt", 'a')
	file.write("%s;%s;%s;%s\n"%(args))
	file.close()

def lerTodoBancoDeDados():
	lista = []
	file = open("db.txt", 'r')
	linhas = file.readlines()
	file.close()
	for linha in linhas:
		lista.append(linha.strip().split(";"))
	return lista