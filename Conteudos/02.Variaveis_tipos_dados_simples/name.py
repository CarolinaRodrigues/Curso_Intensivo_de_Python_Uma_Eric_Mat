#Strings: As strings à primeira vista, são bem simples, mas você pode usá-las de varios modos diferentes.
#Uma string é simples uma serie de caracteres. Tudo que estiver entre aspas é considerada uma string em Python, e você pode usar aspas simples ou duplas em torno de suas strings, assim: "This is a string." / 'This is also a string
#Essa flexibilidade permite usar aspas e apoóstrofe em suas strings:
# 'I    told my friend, "Python is my favorite language!" '
#  "The language 'Python' is namd afther Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."
#Vamos explorar Algumas maneiras de usar strings.

#Mudando para letra maiúscula em uma string usando métodos.:  Uma das tarefas mais simples que podemos fazer com string é mudar o tipo de letra, isto é, minúscola ou maiúscula, das palavras de uma string. observe o codigo a seguir.

name = "ada lovelace"
print(name.title())
#Exibe cada palavra com Letra maiuscula no inicio

name = "Ada Lovelace"
print(name.upper())
print("\n" + name.lower())

#.upper() Exibe as letras todas em maiúsculo
#.lower() Exibe as letras todas em minúsculo

#Combinando ou concatenando strings Muitas vezes, será conveniente combinar strings. Por exemplo, você pode querer armazenar um primeiro nome e um sobrenome em variáveis separadas e, então, combiná-las quando quiser exibir o nome completo de alguém:

first_name = "ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
#Esse método de combinar string e chamado de concatenação.
print("\n" + full_name)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("\n Hello, " + full_name.title() + "!")

#Podemos usar concatenação para compor uma mensagem e então armazenar a mensagem completa em uma variável:

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "\n Hello, " + full_name.title() + "!"
print(message)