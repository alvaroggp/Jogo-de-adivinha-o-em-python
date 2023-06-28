from random import randint

def exclamacoes(titulo):
    
    tamanho_do_titulo = len(titulo) 

    print("-" * tamanho_do_titulo)
    print(titulo)
    print("-" * tamanho_do_titulo)


soma_dos_pontos = 0
vezes_jogadas = 0

while True:
    pontuacao = 10    
    exclamacoes("Bem vindo ao jogo de adivinhação")

    numero_certo = randint(1, 5)
    numero_do_usuario = int(input('Digite um valor de 1 a 5: '))
    
    while True:
        if numero_certo == numero_do_usuario:
            print(f"Parabens, você acertou, o numero era {numero_certo} :)")
            soma_dos_pontos += pontuacao
            vezes_jogadas += 1
            break
        else: 
            numero_do_usuario = int(input("Que pena você ERROU, tente de novo: "))
            pontuacao -= 2
            continue
     
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
    
media = soma_dos_pontos / vezes_jogadas 
exclamacoes(f"Muito obrigado por jogar, sua media de pontos foi {media:.2f}")
        