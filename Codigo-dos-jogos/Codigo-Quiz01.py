print("SEJA BEM VINDO AO QUIZ DAS ANIMAÇÕES!!")
print(" Qual dos desenhos tem mais episódios? \n A) Hora de aventura \n B) Steven Universo\n C) Ben 10 \n D) Bob Esponja ")
R = str(input("Digite sua resposta: "))
pontos = 0

if R == "D" or R == "d":
    print("Correto! Bob Esponja possui 303 episódios no total")
    pontos += 1
else:
    print("Resposta errada!")
    
print(" \n Qual deles é a animação mais velha? \n A) Coragem o Cão Covarde \n B) Max Steel \n C) Pokémon \n D) Cavaleiros do Zodíaco ")    
R = str(input("Digite sua resposta: "))

if R == "D" or R == "d":
    print("Correto! Cavaleiros do Zodíaco lançou no Japão em 1986, porém só chegou no Brasil em 1994")
    pontos += 1
else:
    print("Resposta errada!")
    
print("\n Qual é o mais recente? \n A) Ursos sem Curso \n B) The Loud House \n C) Clarêncio, o Otimista \n D) My Little Pony")
R = str(input("Digite sua resposta: "))

if R == "B" or R == "b":
    print("Correto! The Loud House fez sua estreia em 2016")
    pontos += 1
else:
    print("Resposta errada!")
    
print("\n Qual foi o mais assistido de 2008 no Brasil? \n A) Ben 10: Força Alienígena \n B) Phineas e Ferb \n C) Avatar: A Lenda de Aang \n D) Naruto")
R = str(input("Digite sua resposta: "))

if R == "A" or R == "a":
    print("Correto! Ben 10 foi o maior sucesso da Cartoon Network na época com recordes de audiência")
    pontos += 1
else:
    print("Resposta errada!")
    
print("\n Complete a frase da abertura de Pokémon: 'Esse é o meu jeito de viver...'\n A) Temos que pegar! \n B) O bem vencer o mal! \n C) E ninguém nunca foi igual \n D) Prepare-se para encrenca")
R = str(input("Digite sua resposta: "))

if R == "C" or R == "c":
    print("Correto! Você teve uma boa infância")
    pontos += 1
else:
    print("Resposta errada!")
    
print("\n Quem é mais velho? \n A) Darwin (Gumball) \n B) Timmy (Padrinhos Mágicos) \n C) Masha (Masha e o Urso) \n D) Piccolo (Dragon Ball)")
R = str(input("Digite sua resposta: "))

if R == "B" or R == "b":
    print("Correto! Timmy na verdade tem 60 anos mas fez um pedido secreto para impedir seu envelhecimento")
    pontos += 1
else:
    print("Resposta errada!")
    
print("\n Qual desses estreou em 2009? \n A) Iron Man: Armored Adventures \n B) Dragon Ball Z \n C) Samurai Jack \n D) Johnny Bravo")
R = str(input("Digite sua resposta: "))

if R == "A" or R == "a":
    print("Correto! A série esquecida do Homem de Ferro lançou esse ano")
    pontos += 1
else:
    print('Resposta errada!')
    
print("\n Em qual desses houve o sacrifício de um personagem querido para salvar o universo inteiro? \n A) O Espetacular Homem-Aranha \n B) Caçadores de Trolls \n C) One Piece \n D) Apenas um Show")
R = str(input("Digite sua resposta: "))

if R == "D" or R == "d":
    print("Correto! No final o Pairulito se sacrifica para impedir a destruição do universo")
    pontos += 1
else:
    print('Resposta errada!')

print("\n!RESULTADOS!")
print(f"{pontos}/8")   

if pontos == 0:
    print("Você é uma pessoa triste que não teve infância...")
elif pontos <= 4:
    print("Você está velho e se esquecendo de bons momentos")
elif pontos == 8:
    print("Parabéns, você é uma lenda")
else:
    print("Boa! Ainda ta com a memória fresca!")