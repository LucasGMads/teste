#Pede a entreda de dois numéros e a operação que será feita
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação (+, -, *, /): ")

#Faz a conta de acordo com a operção escolhida
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        #Faz retornar um erro de divisão pois não divide por zero
    else:
        resultado = "Erro: Divisão por zero não é permitida."
        #Caso digite errado gera uma mensagem de erro 
else:
    resultado = "Operação inválida."

#Impreime o resultado
print("O resultado é:", resultado)