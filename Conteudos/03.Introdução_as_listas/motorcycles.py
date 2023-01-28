#
# Modificando um elemento de uma lista

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Concatenando elementos no final da lista

print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print("\n")
# Criando uma lista vazia

motorcycles1 = []

motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')

print(motorcycles1)

print("\n")

# Inserindo elementos em uma lista /  em qualquer posição

motorcycles1.insert(0, 'ducati')

print(motorcycles1)

# Removendo elementos de uma lista

del motorcycles1[0]
print(motorcycles1)

# Use para remover o primeiro item 'honda'

del motorcycles1[0]

print(motorcycles1)

#Removendo um item com o metodo pop
print(motorcycles1)
popped_motorcycles = motorcycles1.pop()
print(motorcycles1)
print(popped_motorcycles)

# Utilizando pra exibir ultimo item comprado

last_owned = motorcycles.pop(0)
print('The last motorcycles I owned was a ' + last_owned.title() + ".")

print("\n")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')