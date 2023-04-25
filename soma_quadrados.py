def quadrado(x):
	y = x * x
	return y

	
def soma_de_quadrados(x,y,z):
	a = quadrado(x)
	b = quadrado(y)
	c = quadrado(z)
	ola = "Ola"
	return a+b+c


# PROGRAMA PRINCIPAL (MAIN)
a = -5
b = 2
c = 10
resultado1 = soma_de_quadrados(a,b,c)
soma_de_quadrados(14,12,7)
print(resultado1)
print(resultado2) # nao funciona pq nao defini resultado2
print(ola) # não funciona pq variavel ola é uma variavel local