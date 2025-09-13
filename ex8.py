'''
8) Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''
distance = float(input('Type a distance in meters: '))
Km = distance/1000
Hm = distance/100
Dam = distance/10
dm = distance * 10
cm = distance * 100
mm = distance * 1000

print(f'The distance of {distance}m is equal to: ')
print(f'{Km}Km')
print(f'{Hm}Hm')
print(f'{Dam}Dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')