def valida_int(pergunta,min,max):
    x=int(input(pergunta))
    while ((x<min) or (x>max)):
        x=int(input(pergunta))
    return x
def criarArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo,'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('arquivo {} foi criado sucesso!\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a=open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a= open(nomeArquivo,'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo,nomeJogo,nomeVideogame):
    try:
       a=open(nomeArquivo,'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()

arquivo='game.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

while True:
    print('Menu')
    print('1-cadastrar novo item')
    print('2-listar cadastros')
    print('3-Sair')

    op=valida_int('Escolha a opção desejada:',1,3)
    if op == 1:
        print('opcão de cadastrar novo item selecionado...\n')
        nomeJogo=input('Nome do jogo:')
        nomeVideogame=input('Nome do Video game:')
        cadastrarJogo(arquivo,nomeJogo,nomeVideogame)

    elif op == 2:
        print('opcão de listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break