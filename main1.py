from datetime import date


name = 'Mão de Vaca'
print('-' * (len(name) + 15))
print(name.center(25))
print('-' * (len(name) + 15))
print('Seu controlador de gastos.')
print()

saldo = float(input('Quanto você quer gastar no mês?: '))

gastos = []

def resposta():
     resposta_valida = False
     while resposta_valida == False:
          newgasto = input('Gostaria de adicionar um novo gasto?: (s/n).\n')
          if newgasto == 'n' or newgasto == 's':
               resposta_valida = True
               return newgasto
          else:
            print('Digite (s) ou (n).')
     

def add_gasto():

    resposta_usuario = resposta()
    while resposta_usuario == 's':
            valor_valido = False
            while valor_valido == False:       
                    try:
                        gasto = float(input('Digite o valor do gasto: '))
                        if gasto <= 0:
                            print('Valor inválido. Digite novamente.')
                        else:
                            valor_valido = True 
                    except ValueError:
                        print('Erro. Por favor, tente novamente.')   

            nome_gasto = False
            while nome_gasto == False:
                    nome = input('Qual o nome do gasto: ').strip()
                    if nome != '':
                        nome_gasto = True
                    else:
                        print('Coloque um nome válido.')        
            hoje = date.today()
            data_formatada = hoje.strftime('%d/%m/%Y')
            gastos.append({
                           'nome': nome, 'gasto': gasto, 'data': data_formatada
                               })
       
            resposta_usuario = resposta()

def ver_saldo():
    total_gasto = 0
    for gasto in gastos:
        total_gasto = total_gasto + gasto['gasto']

    sobra = saldo - total_gasto
    print(f'Orçamento mensal: R$ {saldo:.2f}.')
    print(f'Total gasto: R$ {total_gasto:.2f}.')

    if sobra <= 0:
        print(f'Saldo disponível: R$ {sobra:.2f}')
        print(f'Atenção! \nVocê ultrapassou seu orçamento mensal em R$ {- sobra:.2f}.\n')
    else:
        print(f'Saldo disponível: R$ {sobra:.2f}\n')
    

def ver_gasto():
    msg_gasto = 'Gastos'
    total_gasto = 0
    print('-' * 5, (msg_gasto), '-' * 5)
    for gasto in gastos:
        print(f'{gasto['nome']}: R$ {gasto['gasto']:.2f} - {gasto['data']}.')
        total_gasto = total_gasto + gasto['gasto']

    print(f'\nTotal Gasto: R$ {total_gasto:.2f}.\n')

menu = ''
while menu != '4':
    menu = input('1 - Adicionar gasto.\n2 - Ver gastos.\n3 - Ver saldo.\n4 - Sair.\n')
    if menu == '1':
        add_gasto()
 
    elif menu == '2':
        ver_gasto()

    elif menu == '3':
        ver_saldo()

    elif menu == '4':
        print('Até mais. :)')

    else:
        print('Opção inválida.')




#fazer o controle desses valores no banco de dados

