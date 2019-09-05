# JOGO DA VELHA - MINIMAX
# AUTOR: LEONARDO COELHO

tab = [' ' for i in range(10)]

#======= FUNCOES ========

#=== JOGADAS ===
def jogadorMov():
    vez = True
    while vez:
        posicao = input('Digite a posicao do movimento (1 ate 9): ')
        posicao = int(posicao)

        if ((vazio(posicao)) and (posicao > 0 and posicao < 10)):
            tab[posicao] = 'X'
            vez = False
        else:
            print('\nMovimento invalido!\n\n')

def iaMov():
    print('move')


#=== VERIFICACOES ===
def vazio(posicao):
    if tab[posicao] == ' ':
        return True
    else:
        return False

def cheio(tab):
    if tab.count(' ') > 1:
        return True
    else:
        return False

def venceu(tabAux, valor):
    if ((tabAux[1] == valor and tabAux[2] == valor and tabAux[3] == valor) or
    (tabAux[4] == valor and tabAux[5] == valor and tabAux[6] == valor) or
    (tabAux[7] == valor and tabAux[8] == valor and tabAux[9] == valor) or
    (tabAux[1] == valor and tabAux[5] == valor and tabAux[9] == valor) or
    (tabAux[3] == valor and tabAux[5] == valor and tabAux[7] == valor) or
    (tabAux[1] == valor and tabAux[4] == valor and tabAux[7] == valor) or
    (tabAux[2] == valor and tabAux[5] == valor and tabAux[8] == valor) or
    (tabAux[3] == valor and tabAux[6] == valor and tabAux[9] == valor)):
        return True
    else:
        return False

#=== OUTRAS FUNCOES ===
def printTab(tab):
    print('-------------')
    print('| ' + tab[1] + ' | ' + tab[2] + ' | ' + tab[3] + ' |')
    print('-------------')
    print('| ' + tab[4] + ' | ' + tab[5] + ' | ' + tab[6] + ' |')
    print('-------------')
    print('| ' + tab[7] + ' | ' + tab[8] + ' | ' + tab[9] + ' |')
    print('-------------')



#======== MAIN ========
print('JOGO DA VELHA - MINIMAX')
printTab(tab)

while not(cheio(tab)):
    # Movimento do Jogador
    if not(venceu(tab, 'O')):
        jogadorMov()
        printTab(tab)
    else:
        print('\n\nCOMPUTADOR VENCEU!!\n\n')
        break

    # Movimento da IA
    if not(venceu(tab, 'X')):
        movVal = iaMov()

        if(movVal == 0):
            print('\n\n EMPATE!!!\n\n')
        else:
            tab[movVal] = 'X'
            printTab(tab)
    else:
        print('\n\nJOGADOR VENCEU!!\n\n')
        break

if cheio(tab):
    print('\n\n EMPATE!!!\n\n')
