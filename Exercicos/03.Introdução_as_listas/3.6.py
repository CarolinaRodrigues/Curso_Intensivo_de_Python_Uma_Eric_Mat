# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
# portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
# • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
# uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
# • Utilize insert() para adicionar um novo convidado no início de sua lista.
# • Utilize insert() para adicionar um novo convidado no meio de sua lista.
# • Utilize append() para adicionar um novo convidado no final de sua lista.
# • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

guest_list = ['philipe', 'edee', 'joao', 'paulo', 'matheos']

guest_list.insert(0, 'alice')

guest_list.insert(3, 'camila')

guest_list.append('bruna')

print("Presenças confirmadas: ")
for list in guest_list:
    print(list.title())