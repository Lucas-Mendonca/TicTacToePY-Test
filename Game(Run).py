from systemGame import Campo
from systemGame import Condicoes_d_vitoria
import os, time
# limpar terminal:
def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# jogo da velha / tic tac toe
limpar()
print("Instrução: X é sempre o primeiro a jogar")
print(" 7 | 8 | 9 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 1 | 2 | 3 ")
time.sleep(3)
limpar()
print("Jogo começa em...")
time.sleep(0.5)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
limpar()
print("Game Start!!!")
campoS = [" "," "," "," "," "," "," "," "," "]
jogador = "X"
jogadas = 0
while 0 == 0:
    limpar()
    print("Turno [[" + jogador + "]]")
    Campo.campoV(campoS[0],campoS[1],campoS[2],campoS[3],campoS[4],campoS[5],campoS[6],campoS[7],campoS[8])
    try:
        print("Realize sua jogada")
        indx = int(input())
        if campoS[indx-1] == " ":
            campoS[indx-1] = jogador
        else:
            int("dawdwadaw")
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
        jogadas = jogadas + 1
    except:
        print("Escolha invalida")
        time.sleep(2)
    finally:
        limpar()
        if jogador == "X":
            jogador2 = "O"
        else:
            jogador2 = "X"
        if Condicoes_d_vitoria.winC(jogador2,campoS[0],campoS[1],campoS[2],campoS[3],campoS[4],campoS[5],campoS[6],campoS[7],campoS[8]) == True:
            print("")
            Campo.campoV(campoS[0],campoS[1],campoS[2],campoS[3],campoS[4],campoS[5],campoS[6],campoS[7],campoS[8])
            time.sleep(4)
            exit()
        if jogadas > 8:
            print("!!! Empate !!!")
            print("")
            Campo.campoV(campoS[0],campoS[1],campoS[2],campoS[3],campoS[4],campoS[5],campoS[6],campoS[7],campoS[8])
            time.sleep(4)
            exit()