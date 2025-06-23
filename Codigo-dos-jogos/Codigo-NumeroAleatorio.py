import random


naleatorio = random.randint(1,100)

while True:
   
    nu = int(input())
   
    if nu == naleatorio:
        txt = "Acertou!"
        print(txt)
        break
    elif nu < naleatorio:
        if naleatorio - nu <10:
            txt = "Numero aleatorio é maior e esta perto"
        else:
            txt = "Numero aleatorio é maior e esta longe"
    else:
        if nu - naleatorio < 10:
            txt = "Numero aleatorio é menor e está perto"
        else:
            txt = "Numero aleatorio é menor e está longe"
    print(txt)