import smtplib
import os
import re
from datetime import datetime, date

def cpf_existente(cpf):
    if cpf in clientes:
        print("CPF já cadastrado")
        return False
    else:
        return True

def valida_cpf(cpf):
    if len(cpf) != 11:
        return False
    cpf = list(cpf)
    for i in range(len(cpf)):
        cpf[i] = int(cpf[i])
    mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    mult2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
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

def valida_telefone(fone):
    if not fone.isdigit():
        return False
    if 8 <= len(fone) <= 11:
        return True
    else:
        return False

def valida_email(email):
    if len(email) <= 5:
        return False
    else:
        if '@' not in email:
            return False
        else:
            if not email.endswith('.com'):
                return False
            else:
                return True

def valida_data(d):
    while not re.match(r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[012]/[12]\d{3})', d):
        d = input("Data inválida!\nDigite uma data válida no formato (xx/xx/xxxx): ")

def valida_uf(a):
    a = a.upper()
    estados = {'AC':[], 'AL':[], 'AM':[], 'AP':[], 'BA':[], 'CE':[], 'DF':[], 'ES':[], 'GO':[], 'MA':[], 'MG':[], 'MS':[], 'MT':[], 'PA':[], 'PB':[], 'PE':[], 'PI':[], 'PR':[], 'RJ':[], 'RO':[], 'RN':[], 'RR':[], 'RS':[], 'SE':[], 'SC':[], 'SP':[], 'TO':[]}
    return a in estados

def altera_dados():
    nome = input("Qual o CPF do cliente que você deseja alterar os dados:")
    if nome in clientes:
        print("O que você pode alterar.")
        print("1 - Fone")
        print("2 - Email")
        print("3 - Data de Nascimento")
        print("4 - Cidade")
        print("5 - Estado")
        opcao22 = input("Digite o que deseja alterar.")

        if opcao22.strip() == '1':
            fone = input("Digite o novo numero")
            while not valida_telefone(fone):
                fone = input("Digite o seu celular = xxxxxxxxxxx ")
                fone.split(' ')
                clientes[nome][1] = fone
            print("Numero alterado com sucesso.")
        elif opcao22.strip() == '2':
            email = input("Digite o novo email.")
            while not valida_email(email):
                email = input("Email inexistente \nDigite o seu email: ")
            clientes[nome][3] = email
            print("Email alterado com sucesso.")
        elif opcao22.strip() == '3':
            nasc = input("Digite a nova data de nascimento XX/XX/XXXXX: ")
            valida_data(nasc)
            clientes[nome][4] = nasc
            print("Data de Nascimento alterado.")
        elif opcao22.strip() == '4':
            cidade = input("Digite a nova cidade: ")
            clientes[nome][5] = cidade
            print("Cidade alterada com sucesso.")
        elif opcao22.strip() == '5':
            estado = input("Digite o novo estado: ")
            while not valida_uf(estado):
                estado = input("Estado Inválido.\nDigite o seu estado: ")
            clientes[nome][6] = estado
            print("Estado alterado com sucesso.")
    else:
        print("Usuario nao existe.")

def apaga_cliente():
    CPF = input("Digite o CPF do cliente que deseja apagar: ")
    if CPF in clientes:
        del clientes[CPF]
        print("Cliente apagado com sucesso")
        grava_clientes()
    else:
        print("Usuario nao cadastrado")

def cadastra_usuario():
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o CPF: ")
    while not valida_cpf(cpf) or not cpf_existente(cpf):
        print("CPF inválido.")
        cpf = input("Digite seu CPF: ")
    fone = input("Digite o seu celular = xxxxxxxxxxx ")
    while not valida_telefone(fone):
        fone = input("Digite o seu celular = xxxxxxxxxxx ")
        fone.split(' ')
    valida_telefone(fone)

    email = input("Digite o seu email: ")
    while not valida_email(email):
        email = input("Email inexistente \nDigite o seu email: ")
    nasc = input("Digite o seu nascimento XX/XX/XXXX: ")
    valida_data(nasc)
    cidade = input("Digite a sua cidade: ")
    estado = input("Digite o seu estado (Sigla): ")
    while not valida_uf(estado):
        estado = input("Estado Inválido.\nDigite o seu estado: ")
    nome = nome
    contadorc = ''
    clientes[cpf] = [nome, fone, cpf, email, nasc, cidade, estado, contadorc]
    grava_clientes()
    print(clientes)
    print("Usuario cadastrado com sucesso")
    os.system("clear")

def pesquisa_clientes():
    nome99 = input("Digite o nome do CPF: ")
    if nome99 in clientes:
        print("Nome: ", clientes[nome99][0])
        print("Fone: ", clientes[nome99][1])
        print("CPF: ", clientes[nome99][2])
        print("Email: ", clientes[nome99][3])
        print("Nascimento: ", clientes[nome99][4])
        print("Cidade: ", clientes[nome99][5])
        print("Estado: ", clientes[nome99][6])
    else:
        print("Usuario nao cadastrado")

def verifica_codigo(codigo):
    return codigo not in fantasias

def cadastrar_fantasia():
    codigo = input("Digite o codigo da fantasia: ")
    while not verifica_codigo(codigo):
        print("Codigo já existente.")
        codigo = input("Digite um novo codigo: ")
    nome = input("Digite o nome da fantasia: ")
    tamanho = input("Digite o tamanho da fantasia: ")
    cor = input("Digite a cor da fantasia: ")
    valor = input("Digite o valor da fantasia: ")
    estoque = input("Digite a quantidade em estoque: ")
    fantasias[codigo] = [nome, tamanho, cor, valor, estoque]
    grava_fantasias()
    print("Fantasia cadastrada com sucesso")

def lista_fantasias():
    print("Lista de Fantasias")
    print("------------------")
    for f in fantasias:
        print("Código:", f)
        print("Nome:", fantasias[f][0])
        print("Tamanho:", fantasias[f][1])
        print("Cor:", fantasias[f][2])
        print("Valor:", fantasias[f][3])
        print("Estoque:", fantasias[f][4])
        print("------------------")

def altera_fantasias():
    codigo = input("Digite o codigo da fantasia que você deseja alterar:")
    if codigo in fantasias:
        print("O que você pode alterar.")
        print("1 - Nome")
        print("2 - Tamanho")
        print("3 - Cor")
        print("4 - Valor")
        print("5 - Estoque")
        opcao2 = input("Digite o que deseja alterar.")

        if opcao2.strip() == '1':
            nome = input("Digite o novo nome")
            fantasias[codigo][0] = nome
            print("Nome alterado com sucesso.")
        elif opcao2.strip() == '2':
            tamanho = input("Digite o novo tamanho.")
            fantasias[codigo][1] = tamanho
            print("Tamanho alterado com sucesso.")
        elif opcao2.strip() == '3':
            cor = input("Digite a nova cor.")
            fantasias[codigo][2] = cor
            print("Cor alterada com sucesso.")
        elif opcao2.strip() == '4':
            valor = input("Digite o novo valor.")
            fantasias[codigo][3] = valor
            print("Valor alterado com sucesso.")
        elif opcao2.strip() == '5':
            estoque = input("Digite o novo estoque.")
            fantasias[codigo][4] = estoque
            print("Estoque alterado com sucesso.")
    else:
        print("Fantasia nao existe.")

def apaga_fantasia():
    codigo = input("Digite o codigo da fantasia que deseja apagar: ")
    if codigo in fantasias:
        del fantasias[codigo]
        print("Fantasia apagada com sucesso")
        grava_fantasias()
    else:
        print("Fantasia nao existe.")

def cadastrar_venda():
    cpf = input("Digite o CPF do cliente: ")
    if cpf in clientes:
        print("Fantasias Disponíveis")
        lista_fantasias()
        codigo = input("Digite o código da fantasia desejada: ")
        if codigo in fantasias:
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade <= int(fantasias[codigo][4]):
                total = quantidade * float(fantasias[codigo][3])
                print("Total da compra: R$", total)
                opcao_pagamento = input("Digite a forma de pagamento (dinheiro ou cartao): ")
                if opcao_pagamento.lower() == 'dinheiro' or opcao_pagamento.lower() == 'cartao':
                    data_venda = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    vendas.append([cpf, codigo, quantidade, total, opcao_pagamento, data_venda])
                    fantasias[codigo][4] = str(int(fantasias[codigo][4]) - quantidade)
                    print("Venda realizada com sucesso")
                    grava_vendas()
                    grava_fantasias()
                else:
                    print("Forma de pagamento inválida")
            else:
                print("Quantidade em estoque insuficiente")
        else:
            print("Código de fantasia inválido")
    else:
        print("CPF não cadastrado")

def lista_vendas():
    print("Lista de Vendas")
    print("---------------")
    for venda in vendas:
        print("CPF do Cliente:", venda[0])
        print("Código da Fantasia:", venda[1])
        print("Quantidade:", venda[2])
        print("Total:", venda[3])
        print("Forma de Pagamento:", venda[4])
        print("Data da Venda:", venda[5])
        print("---------------")

def grava_clientes():
    with open('clientes.txt', 'w') as file:
        for cliente in clientes:
            file.write(f"{cliente},{','.join(clientes[cliente])}\n")

def grava_fantasias():
    with open('fantasias.txt', 'w') as file:
        for fantasia in fantasias:
            file.write(f"{fantasia},{','.join(fantasias[fantasia])}\n")

def grava_vendas():
    with open('vendas.txt', 'w') as file:
        for venda in vendas:
            file.write(f"{','.join(map(str, venda))}\n")

def carrega_clientes():
    if os.path.exists('clientes.txt'):
        with open('clientes.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                clientes[data[0]] = data[1:]

def carrega_fantasias():
    if os.path.exists('fantasias.txt'):
        with open('fantasias.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                fantasias[data[0]] = data[1:]

def carrega_vendas():
    if os.path.exists('vendas.txt'):
        with open('vendas.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                vendas.append(data)

clientes = {}
fantasias = {}
vendas = []

carrega_clientes()
carrega_fantasias()
carrega_vendas()

opcao = ''

while opcao != '0':
    print("1 - Cadastrar Cliente")
    print("2 - Alterar Dados do Cliente")
    print("3 - Apagar Cliente")
    print("4 - Pesquisar Cliente")
    print("5 - Cadastrar Fantasia")
    print("6 - Alterar Dados da Fantasia")
    print("7 - Apagar Fantasia")
    print("8 - Listar Fantasias")
    print("9 - Cadastrar Venda")
    print("10 - Listar Vendas")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastra_usuario()
    elif opcao == '2':
        altera_dados()
    elif opcao == '3':
        apaga_cliente()
    elif opcao == '4':
        pesquisa_clientes()
