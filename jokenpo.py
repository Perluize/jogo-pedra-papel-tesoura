#Usamos a função print() para exibir o boas-vindas na tela

print("--"*25)
print("JOGO PEGRA, PAPEL E TESOURA")
print("--"*25)
print("Bem vindo -- cada jogador deve escolher uma das opções")

#Usamos tuplas para armazenar as informações validas.
opcoes_validas = ("pedra","papel","tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("--"*25)#imprime uma linha para separar

#Usamos a função input() para receber o usuario digita
player_1_inicial = input("Jogador 01, digite sua jogada: ")
player_2_inicial = input("Jogador 02, digite sua jogada: ")

#Usamos .lower() para converter para minusculo e .strip() para remover espaços extras
#Isso evita erros como "Pedra" != "pedra".
player_1 = player_1_inicial.lower().strip()
player_2 = player_2_inicial.lower().strip()

print("--"*25)
print(f"Jogador 01 escolheu:{player_1}")
print(f"Jogador 02 escolheu: {player_2}")
print("--"*25)

#Verificando se as jogadas são validas
if player_1 not in opcoes_validas or player_2 not in opcoes_validas:
    print("Uma ou ambas as jogadas são inválidas! Por favor, use apenas 'pedra', 'papel' ou 'tesoura'.")

#Logica principal do jogo usando comparação(==) e logicos(and, or)
#Caso : EMPATE
elif player_1 == player_2:
    print("RESULTADO: Isto foi um empate!")

#Caso o player 01 vença
elif (player_1 == "pedra" and player_2 == "tesoura") or \
(player_1 == "papel" and player_2 == "pedra" ) or \
(player_1 == "tesoura" and player_2 == "papel"):
    print("RESULTADO : Player 01 VENCEU \O/")

#Caso o player 02 vença
else:
    print("RESULTADO: Parabens!!!  O player02 venceu")

print("--"*25)

print("---------- FIM DE JOGO -----------")
