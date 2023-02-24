# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4 em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.

alien_color = 'yellow'

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
else:
    score = 15

print("O jogador ganhou " + str(score) + " pontos.")