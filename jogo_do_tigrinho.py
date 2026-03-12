import random 
noedas_acerto = 10000000
moedas_ganhas = 90



jogotigre = input("Digite seu nome para começarmos: ");

while True:
    chute = input("quantas rodadas de 1 a 3: ");
    correto = random.randint(1, 3);

    if chute.isdigit() and int(chute) == correto:
        print("Você acertou")
        break
    else:
        tente = input("Quer tentar de novo S/N: ").strip()

        if tente != "S":
            print("Jogo encerrado");
            break