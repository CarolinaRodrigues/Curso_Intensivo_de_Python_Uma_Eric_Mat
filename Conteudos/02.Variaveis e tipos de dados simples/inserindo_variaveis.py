#2. VARIAVEIS E TIPOS DE DADOS SIMPLES...
#Inserindo variaveis em hello world

message = "Hello Python World!!"
print(message)

#Adicione duas novas linhas de código.

message = "Hello Python Crash Course World!!!"
print(message)

#Nomendo e usando Variáveis\ Nomes de variáveis podem conter apenas letras, números e underscores. Podem comecar com uma letra ou underscore, mas não por um numero.EX: message_1, mas não 1_message.
#Espaços não são permitidos em nomes de variaveis, mas underscore podem ser usados para separar palavras em nomes de variáveis. EX: greeting_mesage funciona, mas greeting message, causará erros.
#Evite usar palavras reservadas em nomes de variáveis, ou seja, não use palavras que Python reservou para um propósito partilucar de programação.EX a palavra print.(VEJA A SEÇÃO"PALAVRA RESERVADAS E FUNÇÕES EMBUTIDAS DE PYTHON)
#Nomes de variáveis devem ser concisos, pórem descritivos.EX: name é melhor que n, studente_name é melhor que s_n e name_length é melhor que length_of_persons_name.
#Tome cuidado ao usar a letra minuscula l e a letra maiúscula O, pois elas podem ser confundidas com 1 e 0.
#NOTAS: As variáveis Pyhton que você está usando devem utilizar letras minúsculas,Você não terá erros se usar maiúscula, mas é uma boa ideia evita-las por enquanto.

#Evitando erros

#message = "Hello Python Crash Course reader!!"
#print(mesage)

#TRACEBACK 
# Traceback (most recent call last):
#u File "hello_world.py", line 2, in <module>
#v print(mesage)
#w NameError: name 'mesage' is not defined

mesage = "Hello Python Crash Course reader!"
print(mesage)

