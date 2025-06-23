import random

print("!Jogo de pedra, papel e tesoura!")


while True:
    print("1 - pedra / 2 - papel / 3 - tesoura\nSe voce digitar '4' irá acabar a rodada")
    Escolha = int(input("Escolha sua forma: "))
    Pc = random.randint(1,3)
   
    if(Escolha == 1 and Pc == 3):
        print("Você venceu!!! \n Pedra amassa tesoura\n")
       
    elif(Escolha == 1 and Pc == 2):
        print("Você perdeu!!! \n Papel embrulha pedra\n")
       
    elif(Escolha == 1 and Pc == 1):
        print("Deu empate!!!\n")
       
    elif(Escolha == 2 and Pc == 1):
        print("Você venceu!!! \n Papel embrulha pedra\n")
       
    elif(Escolha == 2 and Pc == 2):
        print("Deu empate!!!\n")
       
    elif(Escolha == 2 and Pc == 3):
        print("Você perdeu!!! \n Tesoura corta o papel\n")
       
    elif(Escolha == 3 and Pc == 1):
        print("Você perdeu!!! \n Pedra amassa tesoura\n")
       
    elif(Escolha == 3 and Pc == 2):
        print("Você venceu!!! \n Tesoura corta o papel\n")
   
    elif Escolha == 4:
        break
       
    else:
        print("Deu empate!!!\n")