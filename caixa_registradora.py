#LISTA QUE PERMITE ADICIONAR PREÇO E NOME DO PRODUTO
lista_prod = []

#FUNÇÃO QUE PERMITE AO USUARIO ADICIONAR PRODUTOS E PREÇO
def adicionar_produto():
  produto = str(input('Digite o produto: '))
  preço = float(input('Digite o preço: '))
  estoque = {'nome_produto': produto , 'valor_preço': preço}
  lista_prod.append(estoque)

#FUNÇÃO QUE PERMITE CALCULAR DESCONTO
def calcular_desconto(total, percentual):
  desconto = total - (total * percentual / 100)
  return desconto

#FUNÇÃO QUE PERMITE EXIBIR RECIBO
def exibir_recibo():
  for estoque in lista_prod:
    print(estoque['nome_produto'])
    print(estoque['valor_preço'])
  total = sum(item['valor_preço'] for item in lista_prod)
  percentual = float(input('Qual valor do desconto? '))
  print(f'Total com desconto: R$ {calcular_desconto(total, percentual):.2f}')


#MENU PRINCIPAL - PERMITE AO USUARIO NAVEGAR ENTRE AS OPÇÕES
menu = True

while menu == True:
  print('1 → Adicionar produto')
  print('2 → Exibir recibo')
  print('3 → Sair')

  opcao = input('O que deseja fazer? ')
  if opcao == '1':
    adicionar_produto()
  elif opcao == '2':
    exibir_recibo()
  else:
    break

    

