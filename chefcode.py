import os
import val
import pickle

receitas = {
    1: {
        'atividade':
        True,
        'nome':
        'Bolo de cenoura',
        'autor':
        'ChefCode',
        'porções':
        10,
        'ingredientes': [{
            'quantidade': 3,
            'medidas': 'unidades',
            'ingrediente': 'Cenouras médias'
        }, {
            'quantidade': 1 / 2,
            'medidas': 'xícara',
            'ingrediente': 'Óleo'
        }, {
            'quantidade': 3,
            'medidas': 'unidades',
            'ingrediente': 'Ovos'
        }, {
            'quantidade': 2,
            'medidas': 'xícara',
            'ingrediente': 'Açúcar'
        }, {
            'quantidade': 2,
            'medidas': 'xícara',
            'ingrediente': 'Farinha de trigo'
        }, {
            'quantidade': 1 / 2,
            'medidas': 'colher de chá',
            'ingrediente': 'Fermento'
        }],
        'passos': [
            'Lave as cenouras e rale-as.',
            'Adicione as cenouras raladas ao liquidificador ou processador',
            'Acrescente o óleo, os ovos e o açúcar.',
            'Passe tudo para uma tigela',
            'Adicione a farinha de trigo e o fermento.',
            'Despeje a massa em uma forma untada e enfarinada.',
            'Asse em forno médio (180°C), preaquecido, por cerca de 40 minutos.'
        ]
    },
    2: {
        'atividade':
        True,
        'nome':
        'Brigadeiro',
        'autor':
        'ChefCode',
        'porções':
        12,
        'ingredientes': [
            {
                'quantidade': 390,
                'medidas': 'ml',
                'ingrediente': 'Leite condensado'
            },
            {
                'quantidade': 3,
                'medidas': 'colher de sopa',
                'ingrediente': 'Achocolatado'
            },
            {
                'quantidade': 1,
                'medidas': 'colher de sopa',
                'ingrediente': 'Manteiga'
            },
        ],
        'passos': [
            'Despeje o leite condensado e o achocolatado em uma panela.',
            'Adicione a manteiga e misture bem até obter uma massa homogênea.',
            'Coloque a massa em um recipiente deixe-o esfriar.',
            'Após esfriar, molde os brigadeiros em formato de bolinhas.',
            'Passe os brigadeiros em granulados.(passo opcional)'
        ]
    },
    3: {
        'atividade':
        True,
        'nome':
        'Coxinha',
        'autor':
        'ChefCode',
        'porções':
        5,
        'ingredientes': [{
            'quantidade': 2,
            'medidas': 'xícaras',
            'ingrediente': 'Farinha de trigo'
        }, {
            'quantidade': 1,
            'medidas': 'xícara',
            'ingrediente': 'Leite'
        }, {
            'quantidade': 1,
            'medidas': 'colher de chá',
            'ingrediente': 'Sal'
        }, {
            'quantidade': 1,
            'medidas': 'colher de chá',
            'ingrediente': 'Temperos a sua escolha'
        }, {
            'quantidade': 2,
            'medidas': 'unidades',
            'ingrediente': 'Ovos para empanar'
        }, {
            'quantidade': 1,
            'medidas': 'xícara',
            'ingrediente': 'Óleo para fritar'
        }, {
            'quantidade': 1,
            'medidas': 'xícara',
            'ingrediente': 'Farinha de rosca'
        }, {
            'quantidade': 1,
            'medidas': 'xícara',
            'ingrediente': 'Recheio a sua escolha'
        }],
        'passos': [
            'Misture o leite com os temperos em fogo baixo.',
            'Adicione a farinha aos poucos até formar uma massa.',
            'Deixe a massa descansar por 30 minutos.',
            'Abra a massa em formato de disco e coloque o recheio no centro.',
            'Feche a massa em formato de coxinha.',
            'Passe nos ovos batidos em um prato raso.',
            'Passe a coxinha na farinha de rosca.',
            'Frite a coxinha em óleo quente até dourar.',
        ]
    },
    4: {
        'atividade':
        True,
        'nome':
        'Empada ',
        'autor':
        'ChefCode',
        'porções':
        5,
        'ingredientes': [{
            'quantidade': 1,
            'medidas': 'xícaras',
            'ingrediente': 'Farinha de trigo'
        }, {
            'quantidade': 5,
            'medidas': 'colheres de sopa',
            'ingrediente': 'Manteiga'
        }, {
            'quantidade': 300,
            'medidas': 'gramas',
            'ingrediente': 'Recheio a sua escolha'
        }, {
            'quantidade': 1,
            'medidas': 'unidade',
            'ingrediente': 'Ovo para pincelar'
        }],
        'passos': [
            'Misture a farinha com a manteiga até formar uma massa.',
            'Abra a massa em formato de disco, coloque na forminha e adicione o recheio no centro.',
            'Feche a massa com um circulo em cima.',
            'Bata o ovo em um prato raso. (para misturar a clara e a gema)',
            'Pincele ovo por cima da empada. (só na parte de cima)'
        ]
    },
    5: {
        'atividade':
        True,
        'nome':
        'Capuccino',
        'autor':
        'ChefCode',
        'porções':
        2,
        'ingredientes': [{
            'quantidade': 400,
            'medidas': 'ml',
            'ingrediente': 'Leite'
        }, {
            'quantidade': 2,
            'medidas': 'colheres de sopa',
            'ingrediente': 'Café solúvel'
        }, {
            'quantidade': 2,
            'medidas': 'colheres de sopa',
            'ingrediente': 'Açucar (opicional)'
        }, {
            'quantidade': 1,
            'medidas': 'colher de sopa',
            'ingrediente': 'Chocolate em pó'
        }, {
            'quantidade': 1,
            'medidas': 'pitada',
            'ingrediente': 'Canela (opicional)'
        }],
        'passos': [
            'Coloque o leite e o café solúvel em um copo junto com a água quente.',
            'Adicione o açucar e a canela.',
            'Mexa até que o café esteja completamente dissolvido.',
            'Adicione o chocolate em pó.',
            'Mexa até que o chocolate esteja completamente dissolvido.',
            'Despeje o capuccino em um copo e sirva.'
        ]
    },
    6: {
        'atividade':
        True,
        'nome':
        'Suco',
        'autor':
        'ChefCode',
        'porções':
        5,
        'ingredientes': [{
            'quantidade': 2,
            'medidas': 'xícaras',
            'ingrediente': 'Água gelada'
        }, {
            'quantidade': 1,
            'medidas': 'xícara',
            'ingrediente': 'Fruta desejada'
        }, {
            'quantidade': 1,
            'medidas': 'colher de chá',
            'ingrediente': 'Adoçante a sua escolha'
        }, {
            'quantidade': 5,
            'medidas': 'unidades',
            'ingrediente': 'Cubos de gelo (opicional)'
        }],
        'passos': [
            'Bata a fruta desejada no liquidificador juntamente com a água',
            'Despeje em um recipiente para coar',
            'Adicione o adoçante e os cubos de gelo.',
            'Despeje o suco em um copo e sirva.'
        ]
    },
}

nome_id = {
    'bolo de cenoura': 1,
    'brigadeiro': 2,
    'coxinha': 3,
    'empada': 4,
    'capuccino': 5,
    'suco': 6
}

#try:
# arq_receitas = open("receitas.dat", "rb")
#receitas = pickle.load(arq_receitas)
#except:
# arq_receitas = open("receitas.dat", "wb")
#arq_receitas.close()

#try:
# arq_nome_id = open("nome_id.dat", "rb")
#nome_id = pickle.load(arq_nome_id)
#except:
# arq_nome-id = open("nome_id.dat", "wb")
#arq_nome_id.close()

######################################### FUNÇÕES ##################################################


def intro():
    print('|------| SIG-Receitas |------|')
    print('|                            |')
    print('|   Bem vindo ao ChefCode!   |')
    print('|                            |')
    print('|____________________________|')
    print()
    print('Aqui você encontra receitas incríveis para você cozinhar em casa!')


def saudacao(usuario):
    os.system('clear')
    print(f'Olá, {usuario}!')


def menu_principal():
    print('Dê uma olhada nas nossas opções:')
    print(' __________________________________')
    print('|                                  |')
    print('|  Opções:                         |')
    print('|__________________________________|')
    print('|  1- Ver nossas receitas          |')
    print('|  2- Cadastrar nova receita       |')
    print('|  3- Editar uma receita           |')
    print('|  4- Seguir uma receita           |')
    print('|  5- Excluir uma receita          |')
    print('|  0- Sair                         |')
    print('|__________________________________|')


def opcao():
    os.system('clear')
    print(' __________________________________')
    print('|                                  |')
    print('|  Opções:                         |')
    print('|__________________________________|')
    print('|  1- Ver nossas receitas          |')
    print('|  2- Cadastrar nova receita       |')
    print('|  3- Editar uma receita           |')
    print('|  4- Seguir uma receita           |')
    print('|  5- Excluir uma receita          |')
    print('|  0- Sair                         |')
    print('|__________________________________|')
    escolha = int(input("Escolha sua opção: "))
    return escolha


def buscar_receita():
    nome_busca = input("Digite o nome da receita: ").lower().strip()
    encontradas = []
    for nome in nome_id:
        if nome.startswith(nome_busca):
            encontradas.append(nome)
    if not encontradas:
        print("Nenhuma receita encontrada.")
        return 0
    if len(encontradas) == 1:
        return nome_id[encontradas[0]]
    print("Receitas encontradas:")
    for i, nome in enumerate(encontradas, start=1):
        print(f"{i} - {nome}")
    escolha = input("Digite o número da receita que deseja: ")
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(encontradas):
            return nome_id[encontradas[escolha - 1]]
    print("Escolha inválida.")
    return 0


def ver_receitas():
    os.system('clear')
    print('Veja as receitas cadastradas:')
    for id_receita, receita in receitas.items():
        if receita['atividade']:
            print(f'{id_receita} - {receita["nome"]}')
    input('Clique em ENTER para voltar ao menu')


def nova_receita():
    os.system('clear')
    print('Você escolheu cadastrar uma nova receita!')
    nome = input('Digite o nome da receita: ').capitalize()
    porcoes = int(input('Quantas porções a sua receita serve? '))
    if porcoes == 0:
        print('O número de porções não pode ser zero!')
    else:
        ingredientes = []
        nome_ing = ''
        while nome_ing.lower() != 'fim':
            nome_ing = input(
                'Digite os ingredientes: (ou digite "fim" para terminar) ')
            if nome_ing.lower() != 'fim':
                quantidade = float(
                    input('Quantidade do ingrediente: (em números) '))
                medidas = input('Medida (xícara, colher, gramas...): ')
                ingr = {
                    "quantidade": quantidade,
                    "medidas": medidas,
                    "ingrediente": nome_ing
                }
                ingredientes.append(ingr)
            else:
                print('Fim da adição de ingredientes!')
        passos = []
        passo = ''
        print('Agora é a vez dos passos')
        while passo.lower() != 'fim':
            passo = input('Digite os passos: (ou digite "fim" para terminar) ')
            if passo.lower() != 'fim':
                passos.append(passo)
        nova_receita = {
            "nome": nome,
            "porções": porcoes,
            "ingredientes": ingredientes,
            "passos": passos,
            "atividade": True,
            "autor": usuario
        }
        ultimo_id = max(receitas.keys()) + 1
        receitas[ultimo_id] = nova_receita
        nome_id[nome.lower()] = ultimo_id
        print(f'A receita: {ultimo_id} - "{nome}" cadastrada com sucesso!')
        input('Clique em ENTER para voltar ao menu')


def edicao():
    os.system('clear')
    print('Você escolheu editar uma receita!')
    print()
    print('___________________________')
    print('|___você__pode__editar:___|')
    print('|                         |')
    print('|  1- O nome              |')
    print('|  2- As porções          |')
    print('|  3- Os ngredientes      |')
    print('|_________________________|')
    ed = int(input('O que você deseja editar? '))
    return ed


def editar_nome():
    print('Você escolheu editar o nome da receita!')
    id_receita = buscar_receita()
    if id_receita == 0:
        input('Clique ENTER para voltar ao menu')
        return
    novo_nome = input('Digite o novo nome da receita: ').strip()
    nome_antigo = receitas[id_receita]['nome'].lower()
    receitas[id_receita]["nome"] = novo_nome
    del nome_id[nome_antigo]
    nome_id[novo_nome.lower()] = id_receita
    print('Receita renomeada com sucesso!')
    input('Clique ENTER para voltar ao menu')


def editar_porcoes():
    print('Você escolheu editar as porções da receita!')
    id_receita = buscar_receita()
    if id_receita == 0:
        input('Clique ENTER para voltar ao menu')
        return

    nova_porcao = int(input('Digite a nova quantidade de porções servidas: '))
    receitas[id_receita]["porções"] = nova_porcao
    print(
        f'As porções da receita "{receitas[id_receita]["nome"]}" foram alteradas com sucesso!'
    )
    input('Clique ENTER para voltar ao menu')


def editar_ingr():
    print('Você escolheu editar os ingredientes da receita!')
    id_receita = buscar_receita()
    if not id_receita:
        input('Clique ENTER para voltar ao menu')
        return
    receita = receitas[id_receita]
    novos_ingr = []
    ing = ''
    while ing.lower() != 'fim':
        ing = input('Digite os ingredientes ou "fim" para terminar: ')
        if ing.lower() != 'fim':
            quantidade = float(
                input('Quantidade do ingrediente: (em números) '))
            medidas = input('Medida (xícara, colher, gramas...): ')
            ingre = {
                "quantidade": quantidade,
                "medidas": medidas,
                "ingrediente": ing
            }
            novos_ingr.append(ingre)
        else:
            print('Fim da adição de ingredientes')
    receitas[id_receita]["ingredientes"] = novos_ingr
    print(
        f'Ingredientes da receita {receitas[id_receita]["nome"]} alterados com sucesso!'
    )
    input('Clique em ENTER para voltar ao menu')


def seguir_receita():
    os.system('clear')
    print('Você escolheu seguir uma receita!')
    id_receita = buscar_receita()
    if not id_receita:
        input('Clique ENTER para voltar ao menu')
        return
    receita = receitas[id_receita]
    if receita['atividade']:
        print(f'\nReceita: {receita["nome"]}')
        print(f'Autor: {receita["autor"]}')
        print(f'Porções: {receita["porções"]}\n')
        print("Ingredientes:")
        for ingr in receita["ingredientes"]:
            print(
                f'- {ingr["quantidade"]} {ingr["medidas"]} de {ingr["ingrediente"]}'
            )
        print("\nModo de preparo:")
        for i, passo in enumerate(receita["passos"], start=1):
            print(f'{i}: {passo}')
    else:
        print(
            "Essa receita está desativada e não pode ser seguida no momento.")
    input('\nPressione ENTER para voltar ao menu')


def excluir_receita(usuario):
    os.system('clear')
    print("Você escolheu excluir uma receita!")
    id_receita = buscar_receita()
    if not id_receita:
        input('Clique ENTER para voltar ao menu')
        return
    receita = receitas[id_receita]
    if receita["autor"] != usuario:
        print(
            'Você não tem permissão para excluir esta receita. Ela pertence a outro usuário.'
        )
        input('Clique ENTER para voltar ao menu')
        return
    if receita['atividade']:
        receita['atividade'] = False
        print(f'Receita "{receita["nome"]}" foi desativada com sucesso.')
    else:
        print(f'A receita "{receita["nome"]}" já está desativada.')
    input('Clique ENTER para voltar ao menu')


def sair():
    print('Obrigado por usar o ChefCode!')
    resp = 'n'
    return resp


########################################## CÓDIGO PRINCIPAL ###############################################################

intro()
usuario = input('Qual seu nome de usuário? ').strip()
saudacao(usuario)
menu_principal()

resp = input('Deseja fazer alguma coisa? (s/n): ').lower().strip()
if resp == 's':
    while resp == 's':
        menu_principal()
        op = opcao()

        if op == 1:  #####################
            ver_receitas()

        elif op == 2:  ###################
            nova_receita()

        elif op == 3:  ###################
            ed = edicao()
            if ed == 1:
                editar_nome()
            elif ed == 2:
                editar_porcoes()
            elif ed == 3:
                editar_ingr()
            else:
                print('Opção inválida!')

        elif op == 4:  ###################
            seguir_receita()

        elif op == 5:  ###################
            excluir_receita(usuario)

        elif op == 0:  ###################
            resp = sair()

elif resp == 'n':
    print('Tudo bem, até a próxima!')
    sair()
else:
    print('Resposta inválida! Use apenas "s" para sim ou "n" para não.')
    
#arq_alunos = open("receitas.dat", "wb")
#pickle.dump(s, arq_receitas)
#arq_receitas.close()

#arq_nome_id = open("nome_id.dat", "wb")
#pickle.dump(s, arq_nome_id)
#arq_nome_id.close()