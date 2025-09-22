num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
operador = input('Digite o operador: ')

if operador == '+':
    resultado = int(num1) + int(num2)
    print('O resultado é:', resultado)
elif operador == '-':
    resultado = int(num1) - int(num2)  
    print('O resultado é:', resultado)
elif operador == '*':
    resultado = int(num1) * int(num2)
    print('O resultado é:', resultado)
elif operador == '/':
    resultado = int(num1) / int(num2)
    print('O resultado é:', resultado)
else:
    resultado = 'Operador inválido'
