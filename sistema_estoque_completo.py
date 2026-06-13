#LISTA QUE OS PRODUTOS VÃO SER ADD
estoque = []

#FUNÇÃO QUE PERMITE ADICIONAR PRODUTOS
def adicionar_produtos():
  produto = str(input('Digite o produto: '))
  quantidade = int(input('Qual a quantidade que deseja adicionar desse produto? '))
  localização = input('Qual a localização? ')
  estoque_prod = {'nome_prod': produto, 'quantid_prod': quantidade, 'loc': localização}
  estoque.append(estoque_prod)

#FUNÇÃO QUE PERMITE REMOVER PRODUTO
def remover_produto():
  produto = str(input('Qual produto deseja remover? '))
  for item in estoque:
    if item['nome_prod'] == produto: 
      estoque.remove(item)

#FUNÇÃO QUE PERMITE BUSCAR PRODUTO
def buscar_produto():
  produto = str(input('Qual produto deseja buscar? '))
  encontrado = False
  for item in estoque:
    if item['nome_prod'] == produto:
        print(item)
        encontrado = True
  if not encontrado:
    print('Produto não encontrado')

#FUNÇÃO QUE EXIBE TODOS OS ITENS DO ESTOQUE COM SUAS RESPECTIVAS QUANTIDADES
def exibir_estoque():
  for estoque_prod in estoque:
    print(f'Seu estoque contém os seguintes produtos {estoque_prod["nome_prod"]} com quantidade {estoque_prod["quantid_prod"]}')

#FUNÇÃO QUE EXIBE UM ALERTA SE A QUANTIDADE DE PRODUTOS FOR MENOR QUE 3
def alerta_estoque():
  for estoque_prod in estoque:
    if estoque_prod['quantid_prod'] < 3:
      print('Estoque abaixo do ideal, por favor repor ')
    else:
      print('Estoque ideal!')


#MENU QUE PERMITE O USUARIO NAVEGAR ENTRE AS OPÇÕES

menu = True

while menu == True:
  print('1 → Adicionar produto')
  print('2 → Remover produto')
  print('3 → Buscar produto')
  print('4 → Exibir estoque')
  print('5 → Alerta de estoque baixo')
  print('6 → Sair')

  opcao = input('O que deseja? ')
  if opcao == '1':
    adicionar_produtos()
  elif opcao == '2':
    remover_produto()
  elif opcao == '3':
    buscar_produto()
  elif opcao == '4':
    exibir_estoque()
  elif opcao == '5':
    alerta_estoque()
  else:
    break  






  



