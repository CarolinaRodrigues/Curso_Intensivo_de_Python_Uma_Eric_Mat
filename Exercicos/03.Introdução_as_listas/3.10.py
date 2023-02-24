# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
# lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
# cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
# uma lista contendo esses itens e então utilize cada função apresentada neste
# capítulo pelo menos uma vez.

animes_list = ['one piece', 'berserk', 'jujutsu kaisen', 'boku no hero', 'spy family']
message = "my favorite anime is "
for animes in animes_list:
    print(animes.title())
print("\n")
print(message.title() + animes_list[0].title() + ".")

animes_list.append('cyberpunk')

print(animes_list)

animes_list.insert(2, 'chansaw man')

print(animes_list)

del animes_list[4]

print(animes_list)

popped_animes = animes_list.pop()
print(animes_list)
print(popped_animes)

last_anime = animes_list.pop()
print("The last anime I owned was a " + last_anime.title()+ ".")

first_owned = animes_list.pop(0)
print("The first anime I owned was a " + first_owned.title()+ ".")

animes_list.remove('jujutsu kaisen')
print(animes_list)

nao_consigo_terminar = 'berserk'

animes_list.remove(nao_consigo_terminar)
print(animes_list)

anime_list = ['one piece', 'berserk', 'jujutsu kaisen', 'boku no hero', 'spy family']
anime_list.sort()
print(anime_list)
anime_list.sort(reverse=True)
print(anime_list)

print(sorted(anime_list))
print(anime_list)

anime_list.reverse()
print(anime_list)

print(len(anime_list))