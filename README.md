# 🧮 Calculadora Simples em Python

## Descrição
Este projeto implementa uma **calculadora simples em Python**, capaz de realizar operações básicas:  
- **Adição (+)**  
- **Subtração (-)**  
- **Multiplicação (*)**  
- **Divisão (/)**  

O usuário informa dois números e o operador desejado, e o programa retorna o resultado da operação.  

---

## Funcionalidades

- Entrada de **dois números** pelo usuário;
- Entrada de um **operador** (+, -, *, /);
- Verificação de operador inválido;
- Cálculo e exibição do resultado.

---

## Código Principal

```python
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
    print(resultado)
````

---

## Requisitos

* Python 3.x instalado na máquina
* IDE ou editor de texto de sua preferência (VS Code, PyCharm, Thonny, etc.)

---

## Execução

1. Abra o terminal ou console;
2. Navegue até a pasta do arquivo `calculadora.py`;
3. Execute o programa:

```bash
python calculadora.py
```

4. Insira os valores solicitados e o operador desejado.

---

## Exemplo de Uso

```text
Digite um número: 10
Digite outro número: 5
Digite o operador: +
O resultado é: 15
```

```text
Digite um número: 8
Digite outro número: 2
Digite o operador: /
O resultado é: 4.0
```

```text
Digite um número: 4
Digite outro número: 7
Digite o operador: ^
Operador inválido
```

---

## Contribuição

Este projeto é básico e pode ser expandido com funcionalidades como:

* Suporte a números decimais (`float`);
* Operações avançadas (potência, módulo, raiz quadrada);
* Loop para realizar várias operações sem reiniciar o programa;
* Interface gráfica simples (Tkinter, PyQt).

---

## Licença

Uso acadêmico.

Quer que eu faça isso?
```
