lista = []
list(lista)
dados = dict()
dadosm18 = dict()
lista18 = []
dados['nome'] = input('Nome: ').title()
while dados['nome'] != '':
    dados['idade'] = int(input('Idade: '))
    dados['telefone'] = int(input('Telefone: '))
    lista.append(dados.copy())
    dados['nome'] = str(input('Nome: ')).title()
print(f'{"NOME":<15}{"IDADE":<10}{"TELEFONE":<10}')
for contatos in lista:
    print(f'{contatos["nome"]:<15}{contatos["idade"]:<10}{contatos["telefone"]:<10}')
if dados['idade'] < 18:
    lista18.append(dados.copy())
    print('-='*60)
    print('LISTA TELEFÔNICA COM DE MAIOR')
    print(f'{"NOME":<15}{"IDADE":<10}{"TELEFONE":<10}')
    for contatos1 in lista18:
        print(f'{contatos1["nome"]:<15}{contatos1["idade"]:<10}{contatos1["telefone"]:<10}')