import os
from datetime import date
import time
from getpass import getpass

produtos = {}

prox_prod = 1


def verificador():
    while True:
        x = input(f"\nContinuar?(S/N): ").lower()
        if x in ("s", "sim"):
            return "s"
        if x in ("n", "nao", "não"):
            return "n"
        print("Resposta Inválida")


def menu():
    print(f"Gerenciador de Produtos".center(64, "="))
    print(f"1 - Cadastrar produto")
    print(f"2 - Remover produto")
    print(f"3 - Procurar produto")
    print(f"4 - Ver produtos")
    print(f"5 - Sair")


def cadastrar_prod():
    global prox_prod

    continuar = "s"
    while continuar == "s":
        print(f"Cadastrar Produtos".center(64, "="))

        nome_prod = input(f"Digite o nome do produto ou SAIR para sair: ").lower()

        if nome_prod == "sair":
            os.system("cls")
            break

        while True:
            preco_prod = input(f"\nDigite o preço do produto: ")
            try:
                cvt_preco = float(preco_prod)
                break
            except:
                print("\nFormato Inválido")

        while True:
            estoque_prod = input(f"\nDigite quantos produtos estão em estoque: ")
            try:
                cvt_estq = int(estoque_prod)
                break
            except:
                print("\nFormato Inválido")

        data = date.today().strftime("%d/%m/%Y")
        codigo_prod = prox_prod
        produto = {
            "codigo": f"{codigo_prod:04d}",
            "nome": nome_prod,
            "preco": f"R$ {cvt_preco}",
            "estoque": cvt_estq,
            "data_cadastro": data,
        }
        print(
            f"""\nProduto Cadastrado!\n
                Código do Produto: {codigo_prod:04d}
                Nome: {produto['nome']}
                Preço: {produto['preco']}
                Quantidade em estoque: {produto['estoque']}
                Data de Cadastro: {produto['data_cadastro']}"""
        )
        produtos[f"{codigo_prod:04d}"] = produto

        prox_prod += 1

        continuar = verificador()

        if continuar == "n":
            os.system("cls")
            break

        os.system("cls")


def remover_prod():
    while True:

        while True:
            print(f"Remover Produtos".center(64, "="))

            if not produtos:
                print(f"Nenhum produto cadastrado ainda!")
                time.sleep(3)
                os.system("cls")
                return

            procurar = input(
                f"Digite o código do produto a ser removido ou SAIR para sair: "
            )

            if procurar in ("SAIR", "sair"):
                os.system("cls")
                break

            while True:
                try:
                    vct_proc = int(procurar)
                    str_prod = str(f"{vct_proc:04d}")
                    break
                except:
                    print(f"\nFormato Inválido\n")

                procurar = input(f"\nDigite o código do produto a ser removido: ")

            if str_prod not in produtos:
                print("\nProduto não encontrado!")
                time.sleep(3)
                os.system("cls")
            else:
                break

        while True:
            delelatr = input("\nDeseja remover o produto?(S/N): ").lower()
            if delelatr not in ("s", "n", "sim", "nao", "não"):
                print(f"\nResposta Inválida!")
            else:
                break

        if delelatr == "s":
            produtos.pop(str_prod)
            print(f"\n{str_prod} foi removido com sucesso!")

        continuar = verificador()

        if continuar == "n":
            os.system("cls")
            break

        os.system("cls")


def procurar_prod():

    while True:
        print(f"Procurar Produtos".center(64, "="))

        if not produtos:
            print(f"Nenhum produto cadastrado ainda!")
            time.sleep(3)
            os.system("cls")
            return

        procurar = input(
            f"Digite o código do produto a ser verificado ou SAIR para sair: "
        )
        if procurar in ("SAIR", "sair"):
            os.system("cls")
            break

        while True:
            try:
                vct_proc = int(procurar)
                str_prod = str(f"{vct_proc:04d}")
                break
            except:
                print(f"\nFormato Inválido\n")

            procurar = input(f"Digite o código do produto a ser verificado: ")

        if str_prod in produtos:
            print(
                f"""\nProduto Encontrado!\n
                    Código do Produto: {produtos[str_prod]['codigo']}
                    Nome: {produtos[str_prod]['nome']}
                    Preço: {produtos[str_prod]['preco']}
                    Quantidade em estoque: {produtos[str_prod]['estoque']}
                    Data de Cadastro: {produtos[str_prod]['data_cadastro']}"""
            )
        else:
            print("\nProduto não encontrado!")

        continuar = verificador()

        if continuar == "n":
            os.system("cls")
            break

        os.system("cls")


def ver_prod():
    print(f"Produtos Cadastrados".center(64, "="))

    if not produtos:
        print(f"Nenhum produto cadastrado ainda!")
        time.sleep(3)
        os.system("cls")
        return

    for chave, valor in produtos.items():
        print(
            f"\n> CÓDIGO DO PRODUTO: {chave} - - NOME: {valor['nome']} - - PREÇO: {valor['preco']} - - QUANTIDADE EM ESTOQUE: {valor['estoque']} - - DATA DE CADASTRO: {valor['data_cadastro']}"
        )

    getpass(f"\nPressione ENTER para voltar...")
    os.system("cls")


def main():
    opc = 0

    while opc != 5:
        menu()

        opc = int(input(f">> "))

        if opc == 1:
            os.system("cls")
            cadastrar_prod()

        if opc == 2:
            os.system("cls")
            remover_prod()

        if opc == 3:
            os.system("cls")
            procurar_prod()

        if opc == 4:
            os.system("cls")
            ver_prod()


if __name__ == "__main__":
    main()
