'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma
determinada rua. Crie um programa que recebe do usuário um valor que
representa a velocidade e com base nessa velocidade diga se ela tomou
um multa leve, grave ou gravíssima. Levando em consideração que se a
pessoa estiver abaixo da velocidade máxima seu programa deve exibir
"não houve multa", caso esteja até 10km acima, deve exibir: "levou multa
leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir:
"levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,
exiba: "levou multa gravíssima"

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
velocidade atual

2. O que devo fazer com estes dados?
comparar com os limites de velocidade

3. Quais são as restrições deste problema?
se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir
"não houve multa", caso esteja até 10km acima, deve exibir: "levou multa
leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir:
"levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,
exiba: "levou multa gravíssima"

4. Qual é o resultado esperado?
se levou multa, com qual tipo ou se não levou

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
vel_maxima = 80
input vel_atual
if vel_atual <= vel_maxima
    print('Não houve multa')
elif in range(81,90)
    print('Levou multa leve')
elif in range(91,100)
    print('Levou multa grave')
else
    print('Levou multa gravíssima')
'''

vel_maxima = 80
vel_atual = int(input('Digite a sua velocidade: '))

if vel_atual <= vel_maxima:
    print('Não houve multa')
elif vel_atual in range(81,91):
    print('Levou multa leve')
elif vel_atual in range(91,101):
    print('Levou multa grave')
else:
    print('Levou multa gravíssima')