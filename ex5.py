'''
5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5
'''
grade_one = float(input('Grade 1: '))
grade_two = float(input('Grade 2: '))
average = (grade_one + grade_two)/2
print(f'The average between {grade_one} and {grade_two} is {average}')