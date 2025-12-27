# Solicita uma string e um número inteiro como entrada
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado, separada por espaços
resultado = ' '.join([string] * numero)
print(resultado)