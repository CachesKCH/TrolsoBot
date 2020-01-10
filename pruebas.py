def imprime_input(entrada):
    print(entrada)


imprime_input(input("Escribe STR"))


@imprime_input
def suma_cosas(num1, num2):
    result = num1 + num2
    print(result)
