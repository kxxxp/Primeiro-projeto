from datetime import date


def validar_valor(mensagem):
        valor_valido = False
        while not valor_valido:
            try:
                valor = float(input(mensagem))
                if valor <= 0:
                    print('Valor inválido. Digite novamente.')
                else:
                    valor_valido = True
                    return valor
            except ValueError:
                print('Erro. Por favor, tente novamente.')

def validar_nome(mensagem):
    nome_gasto = False
    while not nome_gasto:
        nome = input(mensagem).strip()
        if nome != '':
            nome_gasto = True
            return nome
        else:
            print('Coloque um nome válido.')

def resposta():
     resposta_valida = False
     while not resposta_valida:
          newgasto = input('Adicionar um novo gasto?: (s/n).\n').lower().strip()
          if newgasto in ['s', 'n']:
               resposta_valida = True
               return newgasto
          else:
            print('Digite (s) ou (n).')
     

def add_gasto(gastos):
    resposta_usuario = resposta()
    while resposta_usuario == 's':   
            gasto = validar_valor('Qual o valor do gasto?: ')
            nome = validar_nome('Qual o nome do gasto?: ')        
            hoje = date.today()
            data_formatada = hoje.strftime('%d/%m/%Y')
            gastos.append({
                           'nome': nome, 'gasto': gasto, 'data': data_formatada
                               })
            resposta_usuario = resposta()

def ver_gasto(gastos):
    msg_gasto = 'Gastos'
    total_gasto = 0
    print('-' * 5, (msg_gasto), '-' * 5)
    print()
    for gasto in gastos:
        print(f'{gasto['nome']}: R$ {gasto['gasto']:.2f} - {gasto['data']}.')
        total_gasto = total_gasto + gasto['gasto']
    print(f'\nTotal Gasto: R$ {total_gasto:.2f}.')

def ver_saldo(saldo, gastos):
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


def cabecalho():
    name = 'Mão de Vaca'
    print('-' * (len(name) + 15))
    print(name.center(25))
    print('-' * (len(name) + 15))
    print('Seu controlador de gastos.')
    print()


def mostrar_menu():
    print()
    print('-' * 5, 'MENU', '-' * 5)
    menu_valido = False
    while not menu_valido:
        menu = input('\n1 - Adicionar gasto.\n2 - Ver gastos.\n3 - Ver saldo.\n4 - Sair.\n')
        if menu in ['1', '2', '3', '4']:
            return menu
        else:
            print('Opção inválida.')

def main():
    saldo = validar_valor('Quantos você quer gastar no mês?: ')
    gastos = []
    menu = ''
    while menu != '4':
        menu = mostrar_menu()
        if menu == '1':
            add_gasto(gastos)
        elif menu == '2':
            ver_gasto(gastos)
        elif menu == '3':
            ver_saldo(saldo, gastos)
        elif menu == '4':
            print('Até mais. :)')


cabecalho()
main()

#fazer o controle desses valores no banco de dados

