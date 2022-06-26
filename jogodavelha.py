# Jogo da velha Jefferson teste
import os
import random

class Jogodavelha:
  jogadas = [["","",""],
             ["","",""],
             ["","",""]]

  def jogar(self, simbolo, linha, coluna):
    if self.jogadas[linha][coluna]=="":
      self.jogadas[linha][coluna]=simbolo
      return True
    else:
      return False

  def ganhador(self,simbolo):
    ganha = [ self.jogadas[0][0]+self.jogadas[0][1]+self.jogadas[0][2], 
              self.jogadas[1][0]+self.jogadas[1][1]+self.jogadas[1][2],
              self.jogadas[2][0]+self.jogadas[2][1]+self.jogadas[2][2],
              self.jogadas[0][0]+self.jogadas[1][0]+self.jogadas[2][0], 
              self.jogadas[0][1]+self.jogadas[1][1]+self.jogadas[2][1],
              self.jogadas[0][2]+self.jogadas[1][2]+self.jogadas[2][2],
              self.jogadas[0][0]+self.jogadas[1][1]+self.jogadas[2][2], 
              self.jogadas[0][2]+self.jogadas[1][1]+self.jogadas[2][0] ]
    if  simbolo*3 in ganha:
      return True
    else:
      return False

  def mostrar(self):
    tabuleiro = """
           *********************
          **  Jogo da Velha  **
         *********************

                Coluna
               0   1   2     
             +---+---+---+
        L  0 | 00| 01| 02|
        i    +---+---+---+
        n  1 | 10| 11| 12|
        h    +---+---+---+
        a  2 | 20| 21| 22|
             +---+---+---+
             
             """
    for linha in range(3):
      for coluna in range(3):
        posicao = str(linha)+str(coluna)
        tabuleiro = tabuleiro.replace( posicao,self.jogadas[linha][coluna].ljust(2))
    return tabuleiro    


# Inicio
jogo = Jogodavelha()
jogar = True
jogadas = 1

os.system("cls")
print(jogo.mostrar())

while jogar:
  # usuario joga
  jogador = True
  while jogador:
    posicao = input("Sua vez de jogar informe Linha,Coluna : ")
    linha,coluna = posicao.split(",")
    if jogo.jogar("X",int(linha),int(coluna)):
      jogador = False
  
  jogadas+=1

  os.system("cls")
  print(jogo.mostrar())

  if jogo.ganhador("X"):
    print("Parabens! Voce GANHOU!")
    jogar=False
  else:
    if jogadas<=5:
      # Computador joga
      computador = True
      while computador:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if jogo.jogar("O",linha,coluna):
          computador =  False
      
      os.system("cls")
      print(jogo.mostrar())
      
      if jogo.ganhador("O"):
        print("Que pena! Infelizmente voce PERDEU!")
        jogar=False
    else:
      print("EMPATE! Ninguem ganhou!")
      jogar=False


