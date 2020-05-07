from time import sleep


def leiainteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar um número.\033[m")
            return 0
        else:
            return num


def verpessoas():
    print("PESSOAS:")
    try:
        arquivo = open("pessoas.txt", "rt")
    except FileNotFoundError:
        print("\n\033[31mAparentemente ainda não existe um arquivo.\033[m")
        sleep(1)
    else:
        with open("pessoas.txt") as arquivo:
            for linha in arquivo:
                campo = linha.split(";")
                print(f"|{campo[0]:<30} {campo[1].rstrip():>3} anos|")   # rstrip tira caracter a direita
    print("\n")


def cadastrarpessoas():
    arquivo = open("pessoas.txt", "a")  # "a" abre aquivo (se não existe, cria) e escreve
    arquivo.write(f"{nome};{idade}\n")


while True:
    tamanho = 50
    print("-" * tamanho)
    print("\033[1m1 - Ver pessoas cadastradas:"
            "\n2 - Cadastrar nova pessoa:"
            "\n3 - Sair do sistema:\033[m")
    print("-" * tamanho)
    opcao = leiainteiro("\033[1mSua Opção: \033[m")
    if opcao == 1:
        verpessoas()
    elif opcao == 2:
        nome = str(input("Nome completo: ")).strip()
        idade = leiainteiro("Idade: ")
        cadastrarpessoas()
    elif opcao == 3:
        print("\033[32mObrigado, até outra hora!\033[m")
        break
    else:
        print("\033[31mOpção inválida. Tente novamente\033[m")
