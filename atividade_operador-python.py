# -*- coding: utf-8 -*-
"""atividade-operador.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eZTJ39G7a8Q91iOhWMi4IqWjG3SBgYk7

**Operadores**
"""

x = 6+4*2
print('X =', x)

x=(4*9+5)
print('X =', x)

x=((6+7)*9)
print('X =', x)

x=(15+20-30)
print('X =', x)

x=(6+5**2)
print('X =', x)

"""**Atribuição**"""

x = 8
x += 5
print('X =', x)

x = 8
x -= 4
print('X =', x)

x = 8
x *= 20
print('X =', x)

x = 8
x /=2
print('X =', x)

"""**Comparação**"""

x = 8
x1 = 3
result = x < x1
print(result)

x = 8
x1 = 3
result = x == x1
print(result)

x = 8
x1 = 3
result = x >= x1
print(result)

x = 8
x1 = 3
result = x != x1
print(result)

"""**Identidade**

"""

x1 = "botafogo"
x2 = "flamengo"
x3 = "botafogo"

result = x1 is x3       #False
result0 = x1 is not x2  #True
result1 = x1 is x2      #False
result2 = x2 is not x3  #True

print(f'Os valores são:\n{result}\n{result0}\n{result1}\n{result2}')

"""**Associação**"""

frutas = ["banana","laranja","uva","ameixa"]

x1 = "banana"
x2 = "laranja"
x3 = "abacaxi"

result = x1 in frutas       #True
result0 = x1 not in frutas  #False
result1 = x2 not in frutas  #False
result2 = x3 in frutas      #True

print(f"Os resultados são: \n{result}\n{result0}\n{result1}\n{result}")

x = 4
x1 = 9
x2 = 5

result = (((2 + 5) * 3) + x + 5) < x1                           #False
result0 = (((2 + 5) * 3) + (x + 5 + x1) == (x + 6 + x2 * 2))    #False
result1 = (((3 * 6) + x - 3) < x2)                              #False
result2 = (((7 * 8) > (x + 4 - x1) < (x * 2 + x2 * 9)))         #True
print(f'Os resultados são:\n{result}\n{result0}\n{result1}\n{result2}')

"""**Lógicos**"""

# Utilize operadores lógicos para verificar se um número N está fora do intervalo de 20 e 30.

n = int(input('Digite um número: '))
x = not(n > 20 and n < 30)
print(x)

# Escreve uma expressão lógica que seja True apenas se A for maior do que 10 e B for menor ou igual a 5.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

x = a > 10 and b <= 5

print(x)

# Escreva uma expressão lógica que seja False apenas se A for maior ou igual a 10 ou B for menor do que 5.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

x = not(a >= 10 or b < 5)
print(x)