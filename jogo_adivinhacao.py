from random import randint
from utilitarios import formatador

# Criação de variaveis relacionadas a pontos 
soma_dos_pontos = 0
vezes_jogadas = 0

# Chamando o titulo
formatador("Bem vindo ao jogo de adivinhação")

# loop de central do jogo
while True:
    
    pontuacao = 10 
    numero_certo = randint(1, 5)   
    numero_do_usuario = int(input('Digite um valor de 1 a 5: '))
    
    # Verificando se o jogador venceu ou não
    while True:
        # Finaliza o loop
        if numero_certo == numero_do_usuario:
            print(f"Parabens, você acertou, o numero era {numero_certo}")
            
            # valores para apos a finalização do jogo seja depurado e se chegue a uma media de pontos
            soma_dos_pontos += pontuacao
            vezes_jogadas += 1
            
            # Finalizando o loop de verificação
            break
        
        # Continua o loop
        else: 
            numero_do_usuario = int(input("Que pena você ERROU, tente de novo: "))
            pontuacao -= 2
            continue
     
    # Verificando se o jogador quer jogar denovo 
    resposta = str(input("Quer continuar SIM/NAO:")).upper()
    
    while True:
         
         if resposta == "SIM" or resposta == "NAO":
            break
         
         elif resposta != "SIM" or resposta != "NAO":
            resposta = str(input("Perdao, Responda corretamente SIM/NAO: ")).upper()
            continue
       
    if resposta == "SIM":
        continue
    
    elif resposta == "NAO":
        break 
    
# Calculando a media de pontos do jogador
media = soma_dos_pontos / vezes_jogadas 

formatador(f"Muito obrigado por jogar, sua media de pontos foi {media:.2f}")
        