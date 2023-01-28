# 3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
# jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
# que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir
# uma mensagem para cada pessoa, convidando-a para jantar.


guest_list = ['philipe', 'edee', 'joao', 'paulo', 'luan']
message = "Irei realizar um jantar para alguns amigos, podemos confirmar sua presença "

""" print(message  + guest_list[0].title() + "?")
print(message  + guest_list[1].title() + "?")
print(message  + guest_list[2].title() + "?")
print(message  + guest_list[3].title() + "?")
print(message  + guest_list[4].title() + "?") """

for list in guest_list:
    print(message + list.title() + "??")