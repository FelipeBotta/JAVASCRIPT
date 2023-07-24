print("Olá, Bem-vindo a Calculadora do Botta")

num1 = int(input("Digite o primeiro valor: "))

num2 = int(input("Digite o segundo valor: "))

op = input("Digite a operação desejada: (+, -, * ou /)")
    
if op == "+":
    resultado = num1 + num2
    print("O resultado é {} " .format(resultado))

elif op == "-":
        resultado = num1 - num2
        print("O resultado é {} " .format(resultado))
    
elif op == "/":
        resultado = num1 / num2
        print("O resultado é {} " .format(resultado))

elif op == "*":
        resultado = num1 * num2
        print("O resultado é {} " .format(resultado))

