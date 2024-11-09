```Python
def converter_celsius_para_fahrenheit(celsius):
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

# Exemplo de uso:
temperatura_celsius = 25
temperatura_fahrenheit = converter_celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} graus Celsius equivalem a {temperatura_fahrenheit} graus Fahrenheit.")
```

```Python
def calcular_area_retangulo(largura, altura):
  area = largura * altura
  return area

# Exemplo de uso:
largura_retangulo = 10
altura_retangulo = 5
area_retangulo = calcular_area_retangulo(largura_retangulo, altura_retangulo)
print(f"A área do retângulo é: {area_retangulo}")
```

```Python
def verificar_elemento_na_lista(lista, elemento):

  if elemento in lista:
    return True
  else:
    return False

# Exemplo de uso:
minha_lista = ["maçã", "banana", "laranja"]
elemento_a_buscar = "banana"

if verificar_elemento_na_lista(minha_lista, elemento_a_buscar):
  print(f"O elemento '{elemento_a_buscar}' está na lista.")
else:
  print(f"O elemento '{elemento_a_buscar}' não está na lista.") 
```

```Python
def calculadora(a, b, operacao):
  if operacao == 'soma':
    return a + b
  elif operacao == 'subtracao':
    return a - b
  elif operacao == 'multiplicacao':
    return a * b
  elif operacao == 'divisao':
    if b == 0:
      return 'Divisão por zero não é permitida'
    return a / b
  else:
    return 'Operação inválida'
```
