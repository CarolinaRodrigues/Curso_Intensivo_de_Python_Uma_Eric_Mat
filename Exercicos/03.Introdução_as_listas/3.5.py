#3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar um
# novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
# • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
# no final de seu programa, especificando o nome do convidado que não poderá comparecer.
# • Modifique sua lista, substituindo o nome do convidado que não poderá
# comparecer pelo nome da nova pessoa que você está convidando.
# • Exiba um segundo conjunto de mensagens com o convite, uma para cada
# pessoa que continua presente em sua lista.

guest_list = ['philipe', 'edee', 'joao', 'paulo', 'luan']
convite = "Social com os amigos "
message = "Podemos confirmar sua presença "


for list in guest_list:
    print(convite + message + list.title() + "?")

popped_guest_list = guest_list.pop()
print("O " + popped_guest_list.title() + " não podera comparecer")


guest_list.insert(4, 'matheos')

for list in guest_list:
    print(convite + list.title())

