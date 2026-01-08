lista_completa = []
nome = "a"

while nome != "":
    lista_herois = []
    nome = input("Digite o nome do herói(ou enter para encerrar):")
    if nome == "":
        break
    else: 
        xp_entrada = input("Digite a quantida de xp do herói: ")
        try:
            xp = int(xp_entrada)
            lista_herois.append(nome)
            lista_herois.append(xp)
            lista_completa.append(lista_herois)
            
        except ValueError:
            print("Digite somente números inteiros")

for indice in range (len(lista_completa)):
    heroi = []
    heroi = lista_completa[indice]
    nome_heroi = heroi[0]
    xp_heroi = heroi[1]
    
    if xp_heroi <= 1000:
        xp_heroi = "Ferro"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')
        
    elif xp_heroi <= 2000:
        xp_heroi = "Bronze"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')
        
    elif xp_heroi <= 5000:
        xp_heroi = "Prata"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')

    elif xp_heroi <= 7000:
        xp_heroi = "Ouro"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')

    elif xp_heroi <= 8000:
        xp_heroi = "Platina"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')

    elif xp_heroi <= 9000:
        xp_heroi = "Ascendente"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')

    elif xp_heroi <= 10000:
        xp_heroi = "Imortal"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')
    
    else:
        xp_heroi = "Radiante"
        print (f'O Herói {heroi[0]} está no nível {xp_heroi}')
          
    