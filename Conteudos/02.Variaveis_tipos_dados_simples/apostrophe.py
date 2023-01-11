#Evitando erros de sintaxe com strings
#Um tipo de erro que você poderá ver com certa regularidade é um erro de sintaxe. Um erro de sintaxe ocorre quando Python não reconhece uma seção de seu programa como um código Python válido.
#Eis o modo de usar aspas simples e duplas corretamente.

message = "One of Python's strengths is its diverse community."
print(message)
# O apóstrofo aparece entre um conjunto de aspas duplas, portanto o interpletador Python não terá nenhum problema para ler a string corretamente:

#No entanto, se você usar aspas simples, o interpretador Python não será capaz de identificar em que ponto a string deve terminar:

#message = 'One of Python1's strengths is its diverse community.'
#print(message)

#Você verá a saída a seguir:
#File "apostrophe.py", line 1
#message = 'One of Python's strengths is its diverse community.'
#SyntaxError: invalid syntax

