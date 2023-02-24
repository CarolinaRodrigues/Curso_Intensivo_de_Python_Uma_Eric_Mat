#Comecando com um dicionario vazio

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#Modificando valores em um dicionario

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#Monitorar a posição do alien no jogo

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo comsua
# velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #Este deve ser um alien rápido
    x_increment = 3

 # A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removendo pares de chaves
alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

del alien_0['points']
print(alien_0)