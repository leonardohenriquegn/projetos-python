# SISTEMA DE CADASTRO DE ALUNOS

# Cadastra alunos com notas e calcula média
lista_alunos = []

#FUNÇÃO QUE PERMITE CADASTRAR ALUNOS E SUAS MÉDIAS
def cadastrar_aluno():
  alunos = str(input('Qual nome do aluno? '))
  nota1 = float(input('Digite a primeira nota: '))
  nota2 = float(input('Digite a segunda nota: '))
  nota3 = float(input('Digite a terceira nota: '))
  media = (nota1 + nota2 + nota3) / 3
  aluno = {'nome': alunos, 'notas': [nota1, nota2, nota3], 'media': media}
  lista_alunos.append(aluno)

#FUNÇÃO QUE PERMITE LISTAR OS ALUNOS
def listar_alunos():
  for aluno in lista_alunos:
    aluno['nome']
    aluno['media']
    print(f'{aluno["nome"]} - Média: {aluno["media"]:.2f}')
    if aluno['media'] >= 7:
      print('APROVADO!')
    else:
      print('REPROVADO!')

#MENU QUE PERMITE AO USUARIO O QUE DESEJA
menu = True

while menu == True:
  print('1 ---> CADASTRAR ALUNOS')
  print('2 ---> LISTAR ALUNOS')
  print('3 ---> SAIR')

  opcao = input('O que deseja fazer? ')

  if opcao == '1':
    cadastrar_aluno()
  elif opcao == '2':
    listar_alunos()
  else:
    break



















