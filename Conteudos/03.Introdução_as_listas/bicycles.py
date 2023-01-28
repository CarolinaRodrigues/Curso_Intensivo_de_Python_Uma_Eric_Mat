bicycles = ['trek', 'cannondle', 'redline', 'specialized']
print(bicycles)

print('-------------------------------\n')
#Acessando elementos de uma lista
print(bicycles[0])

print('-------------------------------\n')
#Acessando elementos de uma lista e colocando a primeira letra maiuscula
print(bicycles[0].title())

print('-------------------------------\n')
#Acessando elementos de uma lista
print(bicycles[1])
print(bicycles[3])

print('-------------------------------\n')
#Acessando o ultimo elementos de uma lista
print(bicycles[-1])

print('-------------------------------\n')
#Usando valores individuais de uma lista
bicycles = ['trek', 'cannondle', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)