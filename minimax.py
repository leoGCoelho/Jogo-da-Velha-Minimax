# JOGO DA VELHA - MINIMAX
# AUTOR: LEONARDO COELHO

tab = [' ' for i in range(9)]

#======= FUNCOES ========

#=== TESTE ===
def teste1():
    return [' ' for i in range(10)]

def teste2():
    return [' ', 'X', 'O', 'X', ' ', 'O', 'X', ' ', ' ']

def teste3():
    return ['X', 'O', ' ', 'X', ' ', ' ', ' ', ' ', ' ']

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
    if ((tabAux[0] == valor and tabAux[1] == valor and tabAux[2] == valor) or
    (tabAux[3] == valor and tabAux[4] == valor and tabAux[5] == valor) or
    (tabAux[6] == valor and tabAux[7] == valor and tabAux[8] == valor) or
    (tabAux[0] == valor and tabAux[4] == valor and tabAux[8] == valor) or
    (tabAux[2] == valor and tabAux[4] == valor and tabAux[6] == valor) or
    (tabAux[0] == valor and tabAux[3] == valor and tabAux[6] == valor) or
    (tabAux[1] == valor and tabAux[4] == valor and tabAux[7] == valor) or
    (tabAux[2] == valor and tabAux[5] == valor and tabAux[8] == valor)):
        return True
    else:
        return False

#=== OUTRAS FUNCOES ===
def printTab(tab):
    print('\n-------------')
    print('| ' + tab[0] + ' | ' + tab[1] + ' | ' + tab[2] + ' |')
    print('-------------')
    print('| ' + tab[3] + ' | ' + tab[4] + ' | ' + tab[5] + ' |')
    print('-------------')
    print('| ' + tab[6] + ' | ' + tab[7] + ' | ' + tab[8] + ' |')
    print('-------------')


#========= MAIN ==========
tab = teste1()
printTab(tab)

tab = teste2()
printTab(tab)

tab = teste3()
printTab(tab)
