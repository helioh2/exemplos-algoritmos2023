# Imprima de forma organizada e formatada uma tabela de multiplicação, até 12 x 12.
# Crédito: Isabela

def imprimir_tabela_multiplicacao():
    for i in range(1, 13):
        for j in range(1, 13):
            resultado = i * j
            print("{:3d}".format(resultado), end=" ")
        print()

imprimir_tabela_multiplicacao()


# notas: {:3d} é utilizado para gararntir que cada número seja exibido com 3 espaços reservados
# 'end=" "' é usado para definir um espaço em branco como o caractere final de cada linha