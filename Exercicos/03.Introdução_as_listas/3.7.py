#3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
# mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.
# • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
# mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
# • Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
# apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
# sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
# você sente muito por não poder convidá-la para o jantar.
# • Apresente uma mensagem para cada uma das duas pessoas que continuam na
# lista, permitindo que elas saibam que ainda estão convidadas.
# • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
# tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
# lista vazia no final de seu programa.

guest_list = ['philipe', 'edee', 'joao', 'paulo', 'matheos']

guest_list.insert(0, 'alice')

guest_list.insert(3, 'camila')

guest_list.append('bruna')

print(guest_list)

print("So posso convidar duas pessoa :( ")

message = "Sinto muito não poder convida-la pra o jantar "

popped_guest_list = guest_list.pop(0)
print(message + popped_guest_list.title())
print(guest_list)
print("\n")

popped_guest_list = guest_list.pop(2)
print(message + popped_guest_list.title())

print("\n")

popped_guest_list = guest_list.pop(4)
print(message + popped_guest_list.title())

print("\n")

popped_guest_list = guest_list.pop(2)
print(message + popped_guest_list.title())

print("\n")

popped_guest_list = guest_list.pop(3)
print(message + popped_guest_list.title())

print("\n")

popped_guest_list = guest_list.pop(2)
print(message + popped_guest_list.title())

print("\n")

del guest_list[0]
del guest_list[0]

print(guest_list)