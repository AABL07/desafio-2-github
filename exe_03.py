# Programa para realizar operação simples entre dois números

print("=" * 40)
print("Calculadora Simples")
print("=" * 40)

# Solicitando entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Exibindo opções de operação
print("\nEscolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("\nDigite o número da operação desejada: ")

# Realizando a operação escolhida
if operacao == "1":
    resultado = numero1 + numero2
    print(f"\n{numero1} + {numero2} = {resultado}")
elif operacao == "2":
    resultado = numero1 - numero2
    print(f"\n{numero1} - {numero2} = {resultado}")
elif operacao == "3":
    resultado = numero1 * numero2
    print(f"\n{numero1} × {numero2} = {resultado}")
elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\n{numero1} ÷ {numero2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")
else:
    print("\nOperação inválida!")

print("=" * 40)