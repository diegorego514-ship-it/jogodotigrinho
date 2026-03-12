import random 
noedas_acerto = 10000000
moedas_ganhas = 90
numeros_de_escolhas = 10
numeros_de_tentativas = 15

jogotigre = input("Digite seu nome para começarmos: ");

while True:
    chute = input("Quantas rodadas de 1 a 3: ");
    correto = random.randint(1, 3);

    if chute.isdigit() and int(chute) == correto:
        print("Você acertou")
        break
    else:
        tente = input("Quer tentar de novo S/N: ").strip()

        if tente != "S":
            print("Jogo encerrado");
            break

while True:
    escolhas = input("Quantas escolhas de 1 a 10: ");
    correto = random.randint(1 , 3);

    if escolhas.isdigit() and int(escolhas) == correto:
        print("Você acertou")
        break
    else:
        tente = input("Quer tentar de novo S/N: ").strip()

        if tente != "S":
            print("Jogo encerrado");
