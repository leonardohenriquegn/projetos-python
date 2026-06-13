import random

numero = random.randint(1,100)
tentativas_usadas = 0
usuario = 0

while usuario != numero and tentativas_usadas < 3:
  usuario = int(input('Digite seu número: '))
  if usuario > numero:
    tentativas_usadas += 1
    if tentativas_usadas < 3:
      print(f'O número é menor que {usuario} e você tem somente mais {3 - tentativas_usadas} tentativas')
    
  elif usuario < numero:
    tentativas_usadas += 1
    if tentativas_usadas < 3:
      print(f'O número é maior que {usuario} e você tem somente mais {3 - tentativas_usadas} tentativas')

if numero == usuario:
  print('Parabéns, você ganhou!')
else:
  print(f'Você não tem mais tentativas. O número correto era {numero}')



 







