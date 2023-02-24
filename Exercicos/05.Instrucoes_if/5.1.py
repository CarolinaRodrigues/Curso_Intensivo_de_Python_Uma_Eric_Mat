# 5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma 
# frase que descreva o teste e o resultado previsto para cada um. Seu código deverá ser semelhante a:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Observe atentamente seus resultados e certifique-se de que compreende por que
#cada linha é avaliada como True ou False.
#• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e
#outros cinco avaliados como False.

car = 'subaru'

if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
if car != 'audi':
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

#testes

nome = 'zoro'
if nome == 'zoro':
    print("\nNome == 'zoro'? Verdadeiro")
    print(nome == 'zoro')
if nome != 'sanji':
    print("\nNome == 'sanji'? Falso")
    print(nome == 'sanji')

cidade = 'Manaus'
if cidade == 'Manaus':
    print("\nCidade == 'manaus'? Verdadeiro")
    print(nome == 'Manaus')

if cidade != 'Tefé':
    print("\nCidade == 'Tefé'? Falso")
    print(nome == 'Tefé')

moto = 'honda'
if moto == 'honda':
    print("\nMoto == 'honda'? Verdadeiro")
    print(nome == 'honda')

if moto != '':
    print("\nCidade == 'Tefé'? Falso")
    print(nome == 'Tefé')