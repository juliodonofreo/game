from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def validar_dificuldade(texto: str) -> int:
    while True:
        try:
            dificuldade: int = int(input(texto))
        except ValueError:
            print('a dificuldade deve um numero inteiro. ', end='')
        else:
            if dificuldade < 1 or dificuldade > 4:
                print('a dificuldade deve ser um inteiro entre 1 e 4. ', end='')
            else:
                return dificuldade


def validar_resultado() -> int:
    while True:
        try:
            resultado: int = int(input())
        except ValueError:
            print('o resultado deve ser um número inteiro. ')
        else:
            return resultado


def validar_continuar(texto: str) -> int:
    while True:
        try:
            continuar = int(input(texto))
        except ValueError:
            print('favor digitar um número. ', end='')
        else:
            if continuar not in (0, 1):
                print('digite apenas 0 ou 1. ', end='')
            else:
                return continuar


def jogar(pontos: int) -> None:
    dificuldade: int = validar_dificuldade('Informe o nível de dificuldade desejado (1, 2, 3 ou 4): ')

    calc: Calcular = Calcular(dificuldade)
    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = validar_resultado()

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'você tem {pontos} {"pontos" if pontos > 1 else "ponto"}')

        continuar: int = validar_continuar('Deseja continuar no jogo? [1 - sim, 0 - não] ')

        if continuar:
            jogar(pontos)
        else:
            print(f'você finalizou com {pontos} {"pontos" if pontos > 1 else "ponto"}')
            print('Até a próxima')
    else:
        print(f'você finalizou com {pontos} {"pontos" if pontos > 1 or pontos == 0 else "ponto"}')
        print('Até a próxima')


if __name__ == '__main__':
    main()
