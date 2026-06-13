def calculadora(numero1, numero2, operacao):
  if operacao == '+':
    return (numero1+numero2)
  elif operacao == '-':
    return (numero1-numero2)
  elif operacao == '*':
    return (numero1*numero2)
  elif operacao == '/':
    return(numero1/numero2)
  
historico = []
menu = True

while menu == True:
  print('1 → Somar')
  print('2 → Subtrair')
  print('3 → Multiplicar')
  print('4 → Dividir')
  print('5 → Ver histórico')
  print('6 → Sair')

  opcao = (input('O que deseja fazer? '))
  
  if opcao == '1':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o primeiro número: '))
    operacao = '+'
    resultado = calculadora(numero1, numero2, operacao)
    historico.append(resultado)
    print(f'O resultado da sua operação é igual a: {resultado}')
  
  elif opcao == '2':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o primeiro número: '))
    operacao = '-'
    resultado = calculadora(numero1, numero2, operacao)
    historico.append(resultado)
    print(f'O resultado da sua operação é igual a: {resultado}')
  
  elif opcao == '3':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o primeiro número: '))
    operacao = '*'
    resultado = calculadora(numero1, numero2, operacao)
    historico.append(resultado)
    print(f'O resultado da sua operação é igual a: {resultado}')
  
  elif opcao == '4':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o primeiro número: '))
    operacao = '/'
    resultado = calculadora(numero1, numero2, operacao)
    historico.append(resultado)
    print(f'O resultado da sua operação é igual a: {resultado}')
  
  elif opcao == '5':
    print(f'O seu histórico de contas é esse: {historico}')
  else:
    break
  








  
  