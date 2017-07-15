import smtplib
import os
import re
from datetime import datetime
from datetime import date


def cpfExistente(cpf):
	if cpf in clientes:
		print ("CPF já cadastrado")
		return False
	else:
		return True
		
		
def validaCPF(cpf):
	if len(cpf) != 11:
		return False
	cpf = list(cpf)
	for i in range(len(cpf)):
		cpf[i] = int(cpf[i])
	mult = [10,9,8,7,6,5,4,3,2]
	mult2 = [11,10,9,8,7,6,5,4,3,2]
	soma = 0
	for i in range(len(mult)): 
		soma += cpf[i] * mult[i]
	d1 = 11 - (soma % 11)
	if d1 == 10 or d1 == 11:
		d1 = 0
	soma1 = 0
	for a in range(len(mult2)):
		soma1 += cpf[a] * mult2[a]
	d2 = 11 - (soma1 % 11)	
	if d2 == 10 or d2 == 11:
		d2 = 0
	if d1 == cpf[9] and d2 == cpf[10]:
		return True
	else:
		return False


def validafone(fone):
	if not fone.isdigit():
		return False
	if len(fone) == 9 or len(fone) == 10 or len(fone) ==11 or len(fone) == 8:
		return True
	else:
		return False


def validaemail(email):
	if len(email) <= 5:
		return False
	else:
		if not '@'  in email:
			return False
		else:
			if not email.endswith('.com') :
				return False
			else:
				return True


def validaData(d):
	while bool(re.match('(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012]/[12][0-9]{3})', d)) is False:
		d = input("Data inválida!\nDigite uma data válida no formato (xx/xx/xxxx): ") 	
		

def validaUF(a):
	a = a.upper()
	estados = {'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RO':[],'RN':[],'RR':[],'RS':[],'SE':[],'SC':[],'SP':[],'TO':[]}
	if  a in estados:
		return True	
	else:
		return False


def alteraDados ():
	nome = input ("Qual o CPF do cliente que vc deseja alterar os dados:")
	if nome in clientes:
			print("o que você pode alterar.")
			print("1 - Fone")
			print("2 - Email")
			print("3 - Data de Nascimento")
			print("4 - Cidade")
			print("5 - Estado")
			opcao22  = input("Digite o que deseja alterar.")
			
			if opcao22.strip() == '1':
				fone = input("Digite o novo numero")
				while validafone(fone) == False:
					fone =input("Digite o seu celular = xxxxxxxxxxx ")
					fone.split(' ')
					clientes[nome][1] = fone
				print("Numero alterado com sucesso.")
			elif opcao22.strip() == '2':
				email= input("Digite o novo email.")
				while validaemail(email) == False:
					email =input("Email inexistente \nDigite o seu email: ")
				clientes[nome][3] = email
				print("Email alterado com sucesso.")
			elif opcao22.strip() =='3':
				nasc = input("Digite a nova data de nascimento XX/XX/XXXXX: ")
				validaData(nasc)
				clientes[nome][4] = nasc
				print("Data de Nascimento alterado.")
			elif opcao22.strip() =='4':
				cidade = input("Digite a nova cidade: ")
				clientes[nome][5] = cidade
				print("Cidade alterada com sucesso.")
			elif opcao22.strip() =='5':
				estado = input("Digite o novo estado: ")
				while validaUF(estado) == False:
					estado = input("Estado Inválido.\nDigite o seu estado: ")
				clientes[nome][6] = estado
				print("Estado alterado com sucesso.")
	else:
	  print("Usuario nao existe.")		


def apagaCliente():
		CPF = input("Digite o CPF do cliente que deseja apagar: ")
		if CPF in clientes:
			del clientes[CPF]
			print("Cliente apagado com sucesso")
			grava_clientes()
		else:
			print("Usuario nao cadastrado")


def cadastraUsuario():
	nome =input("Digite o seu nome: ")
	cpf = input("Digite o CPF: ")
	while validaCPF(cpf) == False or cpfExistente(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	fone =input("Digite o seu celular = xxxxxxxxxxx ")
	while validafone(fone) == False:
		fone =input("Digite o seu celular = xxxxxxxxxxx ")
		fone.split(' ')
	validafone(fone)
	
	email =input("Digite o seu email: ")
	while validaemail(email) == False:
		email =input("Email inexistente \nDigite o seu email: ")
	nasc =input("Digite o seu nascimento XX/XX/XXXX: ")
	validaData(nasc)
	cidade =input("Digite a sua cidade: ")
	estado =input("Digite o seu estado (Sigla): ")
	while validaUF(estado) == False:
		estado = input("Estado Inválido.\nDigite o seu estado: ")
	nome= nome
	contadorc =('')
	clientes[cpf] = [nome,fone,cpf,email,nasc,cidade,estado,contadorc]
	grava_clientes()
	print(clientes)
	print("Usuario cadastrado com sucesso")
	os.system ("clear")


def pesquisaClientes():
	nome99 = input("Digite o nome do CPF: ")
	if nome99 in clientes:
		print("Nome: ",clientes[nome99][0])
		print("Fone: ", clientes[nome99][1])
		print("CPF: ",clientes[nome99][2])
		print("Email: ",clientes[nome99][3])
		print("Nascimento: ", clientes[nome99][4])
		print("Cidade: ",clientes[nome99][5])
		print("Estado: ",clientes[nome99][6])
	else:
		print("Usuario nao cadastrado")			


def verificaCodigo(codigo):
	if codigo in fantasias:
		return False
	else: 
		return True


def cadastrarFantasia():
	codigo = input("Digite o código da fantasia. ")
	if verificaCodigo(codigo) == False :
		print("Código inválido")
		while True:
			codigo = input("Digite um novo código")
			if codigo not in fantasias: 
				break
	tipo=input("Digite o tipo da fantasia: ")
	nomeF=input("Digite o nome da fantasia: ")
	preco = input("Digite o preço: ")
	contadorf = ('')
	fantasias[codigo] = [codigo, nomeF, tipo, preco, True, contadorf]
	grava_fantasias()
	print("fantasia Cadastrada com sucesso!")
	os.system ("clear")


def mostrarFantasias(fantasias):
	recuperar_fantasias()
	for i in fantasias:
		if fantasias[i][4] != 'False':
			print("Código: ", fantasias[i][0], "- Nome: ", fantasias[i][1],"Tipo:", fantasias[i][2],"Preço: ", fantasias[i][3])
			print("________________________________________")


def mostrarFantasiasEmprestadas(fantasias):
	recuperar_fantasias()
	for i in fantasias:
		if fantasias[i][4] == 'False':
			print("Código: ", fantasias[i][0], "- Nome: ", fantasias[i][1],"Tipo:", fantasias[i][2],"Preço: ", fantasias[i][3])
			print("________________________________________")


def diff_days2(data):
	data2 = datetime.now().date()
	data = datetime.strptime(data, "%d/%m/%Y").date()
	dif = data2 - data
	dif = dif.days
	return int(dif)


def devolverFantasia():
	print("Essas são as fantasias que foram emprestadas:\n")
	mostrarFantasiasEmprestadas(fantasias)
	devolver = input ("Digite o código correspondente a fantasia a qual você deseja devolver: ")
	while verificaDevolver(devolver) == False:
		devolver = input ("Digite o código de uma fantasia que se encontra emprestada: ")
	data = emprestimos[devolver][2]
	diasAtraso = diff_days2(data)
	if diasAtraso > 0:
		preco = fantasias[devolver][3]
		precoint = float(preco)
		precoTotal = diasAtraso * 2.50 + precoint
		print("Devido a fantasia ter sido entregada após o prazo de entrega, o valor cobrado já com a multa agora é de: %d" %precoTotal)
		print("Se ontem foi feriado ou domingo favor desconsiderar e pagar o valor sem multa")
	fantasias[devolver][4] = True
	print("Fantasia devolvida com sucesso")
	print("Obrigado pela prefêrencia!")
	grava_fantasias()
	historico[fantasias[devolver][1]] = [emprestimos[devolver][0],fantasias[devolver][0], emprestimos[devolver][2], 'Devolvida']
	grava_historico()
	import smtplib
	#Informe suas credenciais abaixo.
	remetente    = "pyfantasypython@gmail.com"
	senha        = "pyfantasy"
 	#Destinatario e informações da mensagem.
	cpf = emprestimos[devolver][0]
	email = clientes[cpf][3]
	destinatario = email
	nome = fantasias[devolver][1]
	assunto      = "Devolucao de fantasias, PY fantasy"
	texto        = "Obrigado por escolher a PY fantasy, a fantasia: " +str(nome)+ " que vossa senhoria alugou foi devolvida com sucesso."
		 
	#Preparando a mensagem
	msg = '\r\n'.join([
	'From: %s' % remetente,
	'To: %s' % destinatario,
	'Subject: %s' % assunto,
	'',
	'%s' % texto
	])
 
	#Enviando o email SMTP esta configurado para o remetete usar Gmail.
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(remetente,senha)
	server.sendmail(remetente, destinatario, msg.encode("utf-8"))
	server.quit()
			

def verificaDevolver(devolver):
	if devolver in emprestimos:
		return True
	else: 
		return False
		

def validaTempoEstimado():
	hj = date.today()
	#print (hj.toordinal())
	futuro = date.fromordinal(hj.toordinal()+7) #+12)  hoje + 45 dias
	futuro = ("%s/%s/%s" % (futuro.day, futuro.month, futuro.year))
	return futuro


def alugar():
	cpf = input("Primeiro indentifique-se, digite o CPF de um cliente cadastrado: ")
	if cpfExistente(cpf) == True:
		print("CPF não cadastrado")
		while cpfExistente(cpf) == True:
			cpf = input("Digite o CPF de um cliente cadastrado: ")
	opcao = '1'
	while opcao.strip() != '0':
		recuperar_fantasias()
		print(clientes[cpf][0])
		print("Essas são as nossas fantasias disponiveis!\n")
		mostrarFantasias(fantasias)
		escolha = input("Digite o código da fantasia a qual você deseja alugar: ")
		if escolha in fantasias:
			fantasias[escolha][5] += "a"
			clientes[cpf][7] += "a"
			data = validaTempoEstimado()
			emprestimos[escolha] = [cpf, escolha, data]
			historico[cpf] = [cpf, escolha, data, 'Alugada']
			
			if escolha in emprestimos:
				fantasias[escolha][4] = False
				grava_fantasias()
				gravaEmprestimo()
				grava_historico()
			opcao = input ("Deseja alugar mais uma fantasia?\n0-NÃO\n1-SIM \n")
			print("Emprestimo realizado com Sucesso, mandaremos um Email com a data de devolução e o valor a pagar!")
			
			import smtplib
			#Informe suas credenciais abaixo.
			remetente    = "pyfantasypython@gmail.com"
			senha        = "pyfantasy"
 
			#Destinatario e informações da mensagem.
			email = clientes[cpf][3]
			destinatario = email
			assunto      = "Aluguel de fantasias, PY fantasy"
			nome = fantasias[escolha][1]
			preco = fantasias[escolha][3]
			texto        = "Obrigado por escolher a PY fantasy, a sua data de devolução é: "+str(data)+ " Se a data de devolução for um domingo ou feriado, favor entregar um dia após. \nE o preço cobrado será de: R$"+str(preco)+ " Pela fantasia: "+str(nome)
		 
			#Preparando a mensagem
			msg = '\r\n'.join([
			'From: %s' % remetente,
			'To: %s' % destinatario,
			'Subject: %s' % assunto,
			'',
			'%s' % texto
			])
		 
			#Enviando o email SMTP esta configurado para o remetete usar Gmail.
			server = smtplib.SMTP("smtp.gmail.com:587")
			server.starttls()
			server.login(remetente,senha)
			server.sendmail(remetente, destinatario, msg.encode("utf-8"))
			server.quit()
		else:
			print("Codigo incorrreto.")
			while escolha not in fantasias:
				escolha = input("Digite o codigo da fantasia desejada.")
	grava_fantasias()
	

def recuperar_clientes():
    with open('clientes.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            clientes[read[2]] = read[:]


def grava_clientes():
    conteudo = ''
    with open('clientes.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in clientes:
            for k in range(len(clientes[i])):
                conteudo += str(clientes[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()


def recuperar_fantasias():
    with open('fantasias.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            fantasias[read[0]] = read[:]


def grava_fantasias():
    conteudo = ''
    with open('fantasias.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in fantasias:
            for k in range(len(fantasias[i])):
                conteudo += str(fantasias[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()


def apagaFantasia():
		mostrarFantasias(fantasias)
		codigo = input("Digite o código da fantasia que deseja apagar: ")
		if codigo in fantasias:
			del fantasias[codigo]
			grava_fantasias()
			print("Fantasia apagada com sucesso")
		else:
			print("Fantasia não cadastrado")


def gravaEmprestimo():
	conteudo = ''
	with open('emprestimos.txt', 'a+') as arquivo:
		arquivo.seek(1)
		arquivo.truncate()
		for i in emprestimos:
			for k in range(len(emprestimos[i])):
				conteudo += str(emprestimos[i][k]) + '|'
			conteudo += '\n'
		arquivo.writelines(conteudo)
	arquivo.close()


def recuperarEmprestimos():
    with open('emprestimos.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            emprestimos[read[1]] = read[:]


def recuperar_historico():
    with open('historico.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            historico[read[1]] = read[:]


def grava_historico():
    conteudo = ''
    with open('historico.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in historico:
            for k in range(len(historico[i])):
                conteudo += str(historico[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()


def mostraHistorico(historico):
	for i in historico:
		a = historico[i][1]
		b = historico[i][0]
		print("CPF do Cliente: ", historico[i][0], "Nome do cliente: ", clientes[b][0], "Código da fantasia: ", historico[i][1], "Nome da fantasia: ", fantasias[a][1]," ", historico[i][3], "Data: ", historico[i][2])

	
def contadorFantasias():
	for i in fantasias:
		tam = fantasias[i][5]
		tam = tam.count('a')
		cod = fantasias[i][0]
		nom = fantasias[i][1]
		grava_historico()
		if tam != 1:
			print("Fantasia código:",cod,"Nome:",nom,"foi alugada",tam,"vezes.")
		else:
			print("Fantasia código:",cod,"Nome:",nom,"foi alugada",tam,"vez.")


def contadorClientes():
	for i in clientes:
		tam = clientes[i][7]
		tam = tam.count('a')
		cpf = clientes[i][2]
		nom = clientes[i][0]
		grava_historico()
		if tam != 1:
			print("Usuario CPF:",cpf,"Nome:",nom,"alugou",tam,"vezes.")
		else:
			print("Usuario CPF:",cpf,"Nome:",nom,"alugou",tam,"vez.")

fantasias = {} 
clientes = {}
emprestimos = {}
historico={}

recuperar_historico()
recuperarEmprestimos()
recuperar_clientes()
recuperar_fantasias()


def centralizar(a):
	print(" "+a.center(70)+" ")

def menuinicial():
	menu = "MENU"
	a = "1-Cadastrar Cliente"
	b = "2-Alterar dados"
	c = "3-Apagar Cliente"
	d = "4-Relatórios"
	e = "5-Cadastrar fantasia"
	f = "6-Consultar fantasias"
	g = "7-Devolver Fantasia"
	h = "8-Apagar fantasia"
	i = "9-Alugar"
	j = "10-Visualizar clientes"
	k = "11-Sair"
	centralizar(menu)
	centralizar(a)
	centralizar(b)
	centralizar(c)
	centralizar(d)
	centralizar(e)
	centralizar(f)
	centralizar(g)
	centralizar(h)
	centralizar(i)
	centralizar(j)
	centralizar(k)

def menuRelatorio():
	a = "1-Fantasias mais alugadas"
	b = "2-Melhores Clientes "
	c = "3-Histórico de alugueis "
	d = "0-Voltar "
	centralizar(a)
	centralizar(b)
	centralizar(c)
	centralizar(d)

def pyfantasy():
	print (' '*18, "━"*38)
	print (' '*17,"│ PyFantasy: Uma locadora de fantasias │")
	print (' '*18, "━"*38)
	print (' '*19,"Desenvolvido por: Hipólito & Miller")
	print()

opcao = '0'
while opcao.strip() != '11':
	pyfantasy()
	menuinicial()
	opcao = input ("Selecione a opção desejada: ")
	if opcao.strip() == '1':
		cadastraUsuario()
	
	elif opcao.strip() == '2':
		alteraDados()
	
	elif opcao.strip() =='3':
	  apagaCliente()
	
	elif opcao.strip() == '4':
		os.system ("clear")		
		while opcao.strip() != '0':
			menuRelatorio()
			opcao = input("Digite a opção desejada: ")
			if opcao.strip() == '1':
				contadorFantasias()
			elif opcao.strip() == '2':
				contadorClientes()
			elif opcao.strip() == '3':
				mostraHistorico(historico)

	elif opcao.strip() == '5':
		cadastrarFantasia()
    
	elif opcao.strip() == '6':
		mostrarFantasias(fantasias)
			
	elif opcao.strip() == '7':
		devolverFantasia()
	
	elif opcao.strip() == '8':
		apagaFantasia()
		
	elif opcao.strip() == '9':
		alugar()

	elif opcao.strip() == '10':
		pesquisaClientes()
