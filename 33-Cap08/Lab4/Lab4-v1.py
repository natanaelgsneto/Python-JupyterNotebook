# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos
 import random

class JogoDaForca:
    def __init__(self, lista_palavras):
        self.lista_palavras = lista_palavras
        self.palavra = self.escolher_palavra()
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.tentativas = 6

    def escolher_palavra(self):
        return random.choice(self.lista_palavras).lower()

    def exibir_palavra(self):
        return ' '.join([letra if letra in self.letras_corretas else '_' for letra in self.palavra])

    def tentar_letra(self, letra):
        letra = letra.lower()
        if letra in self.letras_corretas or letra in self.letras_erradas:
            return "Você já tentou essa letra. Tente outra."
        elif letra in self.palavra:
            self.letras_corretas.add(letra)
            return f"Boa! A letra '{letra}' está na palavra."
        else:
            self.letras_erradas.add(letra)
            self.tentativas -= 1
            return f"Que pena! A letra '{letra}' não está na palavra."

    def ganhou(self):
        return all(letra in self.letras_corretas for letra in self.palavra)

    def jogar(self):
        print("Bem-vindo ao jogo da Forca!")

        while self.tentativas > 0:
            print(f"\nPalavra: {self.exibir_palavra()}")
            print(f"Letras erradas: {', '.join(self.letras_erradas)}")
            print(f"Tentativas restantes: {self.tentativas}")

            tentativa = input("Digite uma letra: ").lower()
            mensagem = self.tentar_letra(tentativa)
            print(mensagem)

            if self.ganhou():
                print(f"\nParabéns! Você adivinhou a palavra: {self.palavra}")
                break
        else:
            print(f"\nFim de jogo! A palavra era: {self.palavra}")

if __name__ == "__main__":
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'desenvolvedor', 'tecnologia']
    jogo = JogoDaForca(palavras)
    jogo.jogar()
