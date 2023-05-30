

olamundo = "Olá Mundo"

print(type(olamundo))

nome = "Fulano"


fruta = "apple"

for idx in range(0, len(fruta)): #0, 1, 2, 3, 4
    currentChar = fruta[idx]  #fruta[0] -> fruta[1] -> fruta[2] -> fruta[4] -> fruta[4]
    print(currentChar + " OBA")

print("\n-------------\n")

fruta = "O operador de indexação (o Python usa colchetes para incluir o índice) seleciona um único caractere de um string. Os caracteres são acessados por sua posição ou valor do índice. Por exemplo, na sequência mostrada abaixo, os 14 caracteres são indexados da esquerda para a direita a partir posição 0 até a posição 13."
for idx in range(len(fruta)-1, -1, -1):
    print(fruta[idx], end="")

print("\n-------------\n")

s = "python rocks"
for idx in range(len(s)):
    if idx % 2 != 0:
        print(s[idx])