import pygame
pygame.init()
repetir = True
def toca_disco():
    mental_nota = 0
    obito_nota = 0
    traffic_nota = 0
    chornea_nota = 0
    print('Qual música você quer ouvir? ')
    print("1 - Mental (Sua nota: {}) \n2 - Traffic Lights (Sua nota: {}) \n3 - Em Óbito (Sua nota: {}) "
          "\n4 - CHORNEA (Sua nota: {})".format(mental_nota, obito_nota, traffic_nota, chornea_nota))
    genero = input('Digite o número equivalente a opção que deseja ouvir: ')
    print("\033[1;35mRelaxe e aproveite o som!\033[m")
    if genero == "1":
        pygame.mixer.music.load('MERTALdemo.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        print("Acabou! Espero que tenha gostado!")
        mental_nota = int(input("De sua nota para essa música: "))
        print("Mental - {}/10".format(mental_nota))

    elif genero == "2":
        pygame.mixer.music.load('traffic lights.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        print("Acabou! Espero que tenha gostado!")
        traffic_nota = int(input("De sua nota para essa música: "))
        print("Traffic Lights - {}/10".format(traffic_nota))
    elif genero == "3":
        pygame.mixer.music.load('Em óbito 1.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        print("Acabou! Espero que tenha gostado!")
        obito_nota = int(input("De sua nota para essa música: "))
        print("Em Óbito - {}/10".format(obito_nota))
    elif genero == "4":
        pygame.mixer.music.load('CHORNEA.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.quit()
        print("Acabou! Espero que tenha gostado!")
        chornea_nota = int(input("De sua nota para essa música: "))
        print("CHORNEA - {}/10".format(chornea_nota))
    else:
        print("escolha apenas os números disponiveis")
while repetir:
    toca_disco()
    while True:
        repetir_pergunta = input("deseja ouvir novamente? (s/n): ")
        if repetir_pergunta.lower() == "s":
            break
        elif repetir_pergunta.lower() == "n":
            repetir = False
            break
        else:
            print("digite apenas 's' ou 'n'!")
