import random
a = [
    "Qual é a capital do Brasil?\nA) Brasília\nB) Rio de Janeiro\nC) São Paulo\nD) Belo Horizonte",
    "Quem escreveu 'Dom Casmurro'?\nA) Machado de Assis\nB) José de Alencar\nC) Clarice Lispector\nD) Graciliano Ramos",
    "Qual é o resultado de 8 x 7?\nA) 56\nB) 49\nC) 64\nD) 63",
    "Em que estado está o Pantanal?\nA) Mato Grosso do Sul\nB) Goiás\nC) Tocantins\nD) Pará",
    "Qual é a principal estrela do nosso sistema solar?\nA) Sol\nB) Vênus\nC) Marte\nD) Saturno"
]

b = [
    "Qual é a fórmula da água?\nA) CO₂\nB) H₂O\nC) O₂\nD) CH₄",
    "Quem pintou 'A Última Ceia'?\nA) Van Gogh\nB) Leonardo da Vinci\nC) Picasso\nD) Michelangelo",
    "Qual é o símbolo químico do ferro?\nA) Fe²\nB) Fe\nC) Ir\nD) F",
    "Quem foi o primeiro presidente do Brasil?\nA) Getúlio Vargas\nB) Deodoro da Fonseca\nC) Juscelino Kubitschek\nD) Floriano Peixoto",
    "Quantos continentes existem?\nA) 5\nB) 7\nC) 6\nD) 8"
]

c = [
    "Qual planeta é conhecido como o planeta vermelho?\nA) Júpiter\nB) Mercúrio\nC) Marte\nD) Netuno",
    "Qual é a função principal do coração?\nA) Controlar hormônios\nB) Produzir sangue\nC) Bombear o sangue\nD) Filtrar toxinas",
    "Qual é o plural de 'pão'?\nA) Pãos\nB) Pãoses\nC) Pães\nD) Pãozes",
    "Quanto é 5²?\nA) 10\nB) 15\nC) 25\nD) 20",
    "Quem descobriu o Brasil?\nA) Cristóvão Colombo\nB) Pedro Álvares de Lima\nC) Pedro Álvares Cabral\nD) Vasco da Gama"
]

d = [
    "Qual é o maior animal terrestre?\nA) Leão\nB) Hipopótamo\nC) Girafa\nD) Elefante",
    "Qual é a unidade de medida da corrente elétrica?\nA) Ohm\nB) Volt\nC) Watt\nD) Ampère",
    "Qual dessas linguagens é usada para criar sites?\nA) Python\nB) Java\nC) C++\nD) HTML",
    "Qual desses planetas é o mais distante do Sol?\nA) Terra\nB) Marte\nC) Urano\nD) Netuno",
    "Qual é a cor resultante da mistura de azul e amarelo?\nA) Roxo\nB) Laranja\nC) Vermelho\nD) Verde"
]

acertos = 0
erros = 0
contador=0

while True:
    contador+=1
    x = random.randint(1,4)
    if x == 1:            
        pergunta = random.choice(a)
        print(pergunta)
        Escolha = input("Qual voce acha que é (Se quiser parar digite 'Z'): ").upper()
        if Escolha == "A":
            print("Acertou\n")
            acertos +=1
        elif Escolha == "Z":
            break
        else:
            print("Errou!\n")
            erros +=1

    if x == 2:
        pergunta = random.choice(b)
        print(pergunta)
        Escolha = input("Qual voce acha que é  (Se quiser parar digite 'Z'):  ").upper()
        if Escolha == "B":
            print("Acertou\n")
            acertos +=1
        elif Escolha == "Z":
            break
        else:
            print("Errou!\n")
            erros +=1

    if x == 3:
        pergunta = random.choice(c)
        print(pergunta)
        Escolha = input("Qual voce acha que é  (Se quiser parar digite 'Z'): ").upper()
        if Escolha == "C":
            print("Acertou\n")
            acertos+=1
        elif Escolha == "Z":
            break
        else:
            print("Errou!\n")
            erros +=1

    if x == 4:
        pergunta = random.choice(d)
        print(pergunta)
        Escolha = input("Qual voce acha que é  (Se quiser parar digite 'Z'): ").upper()
        if Escolha == "D":
            print("Acertou!\n")
            acertos+=1
        elif Escolha == "Z":
            break
        else:
            print("Errou!\n")
            erros +=1
print(f"Acertos: {acertos}\nErros: {erros}\nPorcentagem de acerto: {(100*acertos)/(contador-1)}")