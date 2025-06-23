def campo(linha, coluna):
    campo = []
    for a in range(linha):
        campo.append(coluna * ["O"])  
    return campo

def exibir_campo(campo):
    for linha in campo:
        for celula in linha:
            if celula == "x":
                print("O", end=" ")
            else:
                print(celula, end=" ")
        print()

cam = campo(10, 10)
cam[2][3] = "x"

vidas = 10

for vida in range(vidas):
    print(f"\nTentativa {vida + 1} de {vidas}")
    exibir_campo(cam)
    
    linha_tiro = int(input("Digite a linha (0 a 9): "))
    coluna_tiro = int(input("Digite a coluna (0 a 9): "))

    if linha_tiro < 0 or linha_tiro >= 10 or coluna_tiro < 0 or coluna_tiro >= 10:
        print("Mire dentro do campo!")
        continue

    if cam[linha_tiro][coluna_tiro] == "x":
        print("Acertou! Parabéns")
        cam[linha_tiro][coluna_tiro] = "X"
        break
    else:
        print("Errou!")
        cam[linha_tiro][coluna_tiro] = "*"

print("\nCampo final:")
exibir_campo(cam)
