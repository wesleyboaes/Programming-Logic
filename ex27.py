'''
27) Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média até 4.9: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
score_1 = float(input('Type the first score: '))
score_2 = float(input('Type the second score: '))
average = (score_1 + score_2) / 2

if average < 4.9:
    print('Failed!')
elif average > 7.0:
    print('Passed!')
else:
    print('Retake')