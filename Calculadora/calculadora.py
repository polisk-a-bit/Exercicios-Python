import os
import time
import math


def menu():
    print("Calculadora".center(64, "="))
    print(f"1 - Soma")
    print(f"2 - Subtração")
    print(f"3 - Divisão")
    print(f"4 - Multiplicação")
    print(f"5 - Sair")
    print("=" * 64)


def soma():
    print("Soma".center(64, "="))

    ctr = ""

    while True:

        num1 = input(f"Digite um número base: ")
        num2 = input(f"Digite um outro número para ser somado: ")

        try:
            n1 = int(num1)
            n2 = int(num2)
            resultado = n1 + n2
            print(f"A soma de {n1} + {n2} é {resultado}\n")
            break
        except:
            print(f"Formato inválido\n")

    while ctr != "n":
        ctr = input(f"Continuar somando?(S/N) ").lower()
        if ctr == "n":
            print(f"O resultado final é {resultado}. Retornando ao menu principal...")
            time.sleep(3)
            os.system("cls")
            continue

        elif ctr == "s":
            resultado1 = resultado
            num_ext = input(f"\nDigite um outro número para ser somado: ")
            try:
                n_e = int(num_ext)
                resultado += n_e
                print(f"\nA soma de {resultado1} + {n_e} é {resultado}\n")
            except:
                print(f"Formato inválido\n")

        elif ctr != "n" and "s":
            print(f"Resposta inválida\n")


def subtracao():
    print("Subtração".center(64, "="))

    ctr = ""

    while True:

        num1 = input(f"Digite um número base: ")
        num2 = input(f"Digite um outro número para ser subtraido: ")

        try:
            n1 = int(num1)
            n2 = int(num2)
            resultado = n1 - n2
            print(f"A subtração de {n1} - {n2} é {resultado}\n")
            break
        except:
            print(f"Formato inválido\n")

    while ctr != "n":
        ctr = input(f"Continuar subtraindo?(S/N) ").lower()
        if ctr == "n":
            print(f"O resultado final é {resultado}. Retornando ao menu principal...")
            time.sleep(3)
            os.system("cls")
            continue

        elif ctr == "s":
            resultado1 = resultado
            num_ext = input(f"\nDigite um outro número para ser subtraido: ")
            try:
                n_e = int(num_ext)
                resultado -= n_e
                print(f"\nA subtração de {resultado1} - {n_e} é {resultado}\n")
            except:
                print(f"Formato inválido\n")

        elif ctr != "n" and "s":
            print(f"Resposta inválida\n")


def divisao():
    print("Divisão".center(64, "="))

    ctr = ""

    while True:

        num1 = input(f"Digite um número base: ")
        num2 = input(f"Digite um outro número para ser dividido: ")

        try:
            n1 = int(num1)
            n2 = int(num2)
            try:
                resultado = n1 / n2
                print(f"A divisão de {n1} / {n2} é {resultado}\n")
                break
            except ZeroDivisionError:
                print("O denominador deve ser diferente de zero.\n")
        except:
            print(f"Formato inválido\n")

    while ctr != "n":
        ctr = input(f"Continuar dividindo?(S/N) ").lower()
        if ctr == "n":
            print(f"O resultado final é {resultado}. Retornando ao menu principal...")
            time.sleep(3)
            os.system("cls")
            continue

        elif ctr == "s":
            resultado1 = resultado
            num_ext = input(f"\nDigite um outro número para ser dividido: ")
            try:
                n_e = int(num_ext)
                resultado /= n_e
                print(f"\nA divisão de {resultado1} / {n_e} é {resultado}\n")
            except ZeroDivisionError:
                print("O denominador deve ser diferente de zero.\n")
            except:
                print("Insira um valor válido.\n")

        elif ctr != "n" and "s":
            print(f"Resposta inválida\n")


def multiplicacao():
    print("Multiplicação".center(64, "="))

    ctr = ""

    while True:

        num1 = input(f"Digite um número base: ")
        num2 = input(f"Digite um outro número para ser multiplicado: ")

        try:
            n1 = int(num1)
            n2 = int(num2)
            resultado = n1 * n2
            print(f"A multiplicação de {n1} x {n2} é {resultado}\n")
            break
        except:
            print(f"Formato inválido\n")

    while ctr != "n":
        ctr = input(f"Continuar multiplicando?(S/N) ").lower()
        if ctr == "n":
            print(f"O resultado final é {resultado}. Retornando ao menu principal...")
            time.sleep(3)
            os.system("cls")
            continue

        elif ctr == "s":
            resultado1 = resultado
            num_ext = input(f"\nDigite um outro número para ser multiplicado: ")
            try:
                n_e = int(num_ext)
                resultado *= n_e
                print(f"\nA multiplicação de {resultado1} x {n_e} é {resultado}\n")
            except:
                print(f"Formato inválido\n")

        elif ctr != "n" and "s":
            print(f"Resposta inválida\n")


def main():
    opc = 0

    while opc != 5:
        menu()

        opc = int(input(f">> "))

        if opc == 1:
            os.system("cls")
            soma()
        elif opc == 2:
            os.system("cls")
            subtracao()
        elif opc == 3:
            os.system("cls")
            divisao()
        elif opc == 4:
            os.system("cls")
            multiplicacao()


if __name__ == "__main__":
    main()
