import random

l = ["gumball", "jake", "mordecai", "rick", "clarencio",
"finn", "rigby", "steven", "darwin", "morty"]

pc = random.choice(l)
chance = 0

palavra_certa = ["_" for _ in pc]

while chance < 5:
    print("Palavra atual:", " ".join(palavra_certa))
    if "".join(palavra_certa) == pc:
        print(f"Parabens voce ganhou, essa era a palavra: ", pc)
        break

    Escolha = input("Escolha uma letra para o jogo da forca: ").lower()
    achou = False
    for i in range(len(pc)):
        if pc[i] == Escolha:
            palavra_certa[i] = Escolha
            achou = True
    
    if achou == True:
        print("Existe essa letra na palavra\n")
    else:
        print("Não tem essa letra na palavra\n")
        chance+=1

if "".join(palavra_certa) != pc:
    print(f"Voce não ganhou, a palavra era: {pc}")