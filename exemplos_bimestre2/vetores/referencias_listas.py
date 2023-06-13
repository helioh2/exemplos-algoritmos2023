a = [81, 82, 83]
b = a  # nao cria uma copia da lista, mas sim faz b apontar para o mesmo objeto que a
c = b
print(a is b)

b[0] = 50

print(a)

c[2] = 20

print(a)

a = [1,2,3]   # cria uma nova lista em outro endereço, e faz a apontar para ela

print(a)
print(b)  # a lista apontada por b continua existindo, independente de a

a[0] = 100

print(b)

## DICA: COPIE E COLE ESTE CÓDIGO NO Python Tutor PARA VER PASSO A PASSO
# https://pythontutor.com/python-debugger.html#mode=edit