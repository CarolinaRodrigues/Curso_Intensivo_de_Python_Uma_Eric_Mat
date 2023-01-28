#3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
#simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O
#texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
#personalizada com o nome da pessoa.

friends = ['edee', 'paulo', 'luan', 'ricardo']

message = "Hello my friend "

print(message + friends[0].title() + ".")
print(message + friends[1].title() + ".")
print(message + friends[2].title() + ".")
print(message + friends[3].title() + ".")