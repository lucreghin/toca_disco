import pygame
import json
import os

pygame.init()

ARQUIVO_NOTAS = 'notas.json'

MUSICAS = {
    "1": {"nome": "Mental \033[3m(demo)\033[m", "arquivo": "MENTAL-beta.mp3"},
    "2": {"nome": "Traffic Lights", "arquivo": "traffic lights.mp3"},
    "3": {"nome": "Em Óbito", "arquivo": "Em óbito 1.mp3"},
    "4": {"nome": "CHORNEA", "arquivo": "CHORNEA.mp3"},
}


def carregar_notas():
    if os.path.exists(ARQUIVO_NOTAS):
        with open(ARQUIVO_NOTAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Se o arquivo ainda não existe, começa com nota 0 pra cada música
    return {chave: 0 for chave in MUSICAS}


def salvar_notas(notas):
    with open(ARQUIVO_NOTAS, 'w', encoding='utf-8') as f:
        json.dump(notas, f, ensure_ascii=False, indent=4)


def toca_disco(notas):
    print('Qual música você quer ouvir? ')
    print("1 - {} (Sua nota: {})".format(MUSICAS["1"]["nome"], notas["1"]))
    print("2 - {} (Sua nota: {})".format(MUSICAS["2"]["nome"], notas["2"]))
    print("3 - {} (Sua nota: {})".format(MUSICAS["3"]["nome"], notas["3"]))
    print("4 - {} (Sua nota: {})".format(MUSICAS["4"]["nome"], notas["4"]))

    genero = input('Digite o número equivalente a opção que deseja ouvir: ')

    if genero not in MUSICAS:
        print("escolha apenas os números disponiveis")
        return

    print("\033[1;35mRelaxe e aproveite o som!\033[m")

    musica = MUSICAS[genero]
    pygame.mixer.music.load(musica["arquivo"])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

    print("Acabou! Espero que tenha gostado!")

    while True:
        try:
            nova_nota = int(input("De sua nota para essa música (0-10): "))
            if 0 <= nova_nota <= 10:
                break
            print("Digite um número entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

    notas[genero] = nova_nota
    salvar_notas(notas)
    print("{} - {}/10".format(musica["nome"], nova_nota))


def main():
    notas = carregar_notas()
    repetir = True
    while repetir:
        toca_disco(notas)
        while True:
            repetir_pergunta = input("deseja ouvir novamente? (s/n): ")
            if repetir_pergunta.lower() == "s":
                break
            elif repetir_pergunta.lower() == "n":
                repetir = False
                break
            else:
                print("digite apenas 's' ou 'n'!")
    pygame.quit()


if __name__ == "__main__":
    main()