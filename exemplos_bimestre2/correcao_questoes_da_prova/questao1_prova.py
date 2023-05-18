"""
Escreva um programa que calcula o consumo de gasolina de uma carro 
em quilômetros por litro. O programa deve pedir ao usuário que digite 
o número de quilômetros percorridos e o número de litros de gasolina consumidos. 
Em seguida o programa deve imprimir a resposta.
"""

km = float(input("Digite a quantidade de quilômetros percorridos: "))
litros = float(input("Digite o número de litros consumidos: "))

km_por_litro = km / litros

print(km_por_litro)