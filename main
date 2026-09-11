from datetime import date


name = 'Mão de Vaca'
print('-' * (len(name) + 15))
print(name.center(25))
print('-' * (len(name) + 15))
print('Seu controlador de gastos.')
print()

saldo = float(input('Quanto você quer gastar no mês?: '))

gastos = []

def add_gasto():
    gasto = float(input('Digite o valor do gasto: '))
    nome = input('Qual o nome do gasto: ')
    hoje = date.today()
    data_formatada = hoje.strftime('%d/%m/%Y')
    gastos.append({
                    'nome': nome, 'gasto': gasto, 'data': data_formatada
                })
    newgasto = input('Gostaria de adicionar um novo gasto?: (s/n)')
    while newgasto == 's':
        gasto = float(input('Digite o valor do gasto: '))
        nome = input('Qual o nome do gasto: ')
        hoje = date.today()
        data_formatada = hoje.strftime('%d/%m/%Y')
        gastos.append({
                        'nome': nome, 'gasto': gasto, 'data': data_formatada
                            })
    
        newgasto = input('Gostaria de adicionar um novo gasto?: (s/n)')

def ver_saldo():
    total_gasto = 0
    for gasto in gastos:
        total_gasto = total_gasto + gasto['gasto']

    sobra = saldo - total_gasto
    print(f'Saldo atual: {sobra:.2f}')

def ver_gasto():
    total_gasto = 0
    for gasto in gastos:
        print(f'{gasto['nome']}: R${gasto["gasto"]:.2f} - {gasto['data']}.')
        total_gasto = total_gasto + gasto['gasto']

    print(f'Total Gasto = R$ {total_gasto:.2f}.')

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

