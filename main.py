import csv
import os.path

lista_dict = []

if os.path.exists('contatos.csv'):
    with open('contatos.csv', encoding="utf8") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        for i, linha in enumerate(arquivo_csv):
            if not i == 0:
                contato_dict = {
                    "NOME": linha[0],
                    "TELEFONE": linha[1],
                    "DIA_ANIVERSARIO": linha[2],
                    "MES_ANIVERSARIO": linha[3]
                }
                lista_dict.append(contato_dict)
    print("AGENDA EXISTENTE:")
    print(lista_dict)
    print()
else:
    with open('contatos.csv', 'w', encoding="utf8") as output:
        print("nome,telefone,dia_aniversario,mes_aniversario", file=output)
while True:
    print("(1) Inserir contato")
    print("(2) Remover contato")
    print("(3) Pesquisar contato")
    print("(4) Listar todos os contatos")
    print("(5) Listar contatos que comecem com uma letra específica")
    print("(6) Imprimir os aniversariantes de um mês específico")
    print("(7) Encerrar o programa")
    opcao = int(input())

    if opcao == 1:
        print("Digite o nome do contato")
        nome = input()
        print("Digite o telefone do contato")
        tel = input()
        print("Digite o dia do aniversário do contato")
        while True:
            dia = int(input())
            if not 0 < dia < 32:
                print("Dia inválido")
            else:
                break
        print("Digite o mês do aniversário do contato")
        while True:
            mes = int(input())
            if not 0 < mes < 13:
                print("Mes inválido")
            else:
                break
        contato_dict = {
            "NOME": nome,
            "TELEFONE": tel,
            "DIA_ANIVERSARIO": dia,
            "MES_ANIVERSARIO": mes
        }
        lista_dict.append(contato_dict)
    elif opcao == 2:
        if len(lista_dict) >= 1:
            print("Digite o nome exato do contato a ser removido")
            nome_exato = input()
            achado = 0
            contador = 0
            for i in lista_dict:
                if i["NOME"].upper() == nome_exato.upper():
                    lista_dict.remove(lista_dict[contador])
                    achado = 1
                    break
                contador += 1
            if achado == 1:
                print("Contato removido com sucesso")
            else:
                print("Contato não encontrado")
        else:
            print("A agenda não possui contatos")
    elif opcao == 3:
        if len(lista_dict) >= 1:
            print("Digite o nome exato do contato")
            nome_exato = input()
            achado = 0
            for i in lista_dict:
                if i["NOME"].upper() == nome_exato.upper():
                    print(i)
                    achado = 1
                    break
            if achado == 0:
                print("Contato inexistente")
        else:
            print("A agenda não possui contatos")
    elif opcao == 4:
        if len(lista_dict) >= 1:
            for i in lista_dict:
                print(i['NOME'])
    elif opcao == 5:
        if len(lista_dict) >= 1:
            print("Digite a letra")
            letra = input()
            for i in lista_dict:
                if i['NOME'][0] == letra:
                    print(i['NOME'])
        else:
            print("A agenda não possui contatos")
    elif opcao == 6:
        if len(lista_dict) >= 1:
            print("Digite o mês")
            mes = input()
            for i in lista_dict:
                if i['MES_ANIVERSARIO'] == mes:
                    print(i['NOME'])
        else:
            print("A agenda não possui contatos")
    elif opcao == 7:
        print("Encerrando o programa e salvando no arquivo")
        with open('contatos.csv', 'w', encoding="utf8") as o:
            print("nome,telefone,dia_aniversario,mes_aniversario", file=o)
            for i in lista_dict:
                print(i['NOME'] + "," + i['TELEFONE'] + "," + i['DIA_ANIVERSARIO'] + "," + i["MES_ANIVERSARIO"], file=o)
        break
