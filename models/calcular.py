from random import randint


class Calcular:
    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self.__gerar_valor
        self.__valor2: int = self.__gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 - somar, 2 - subtrair, 3 - multiplicar
        self.__resultado: float = self.__gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'somar'
        elif self.operacao == 2:
            op = 'diminuir'
        elif self.operacao == 3:
            op = 'multiplicar'
        else:
            op = 'operação inválida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def __gerar_valor(self: object) -> int:
        dificuldades = (randint(0, 10), randint(0, 100),
                        randint(0, 1000), randint(0, 10000),
                        randint(0, 100000))
        return dificuldades[self.dificuldade - 1]

    @property
    def __gerar_resultado(self: object) -> int:
        simbolo: str = self._op_simbolo()
        return eval(f'{self.valor1} {simbolo} {self.valor2}')

    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False
        if self.resultado == resposta:
            print('resposta correta! ')
            certo = True
        else:
            print('resposta incorreta!')
            certo = False
        print(f'{self.valor1} {self._op_simbolo()} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo()} {self.valor2} = ?')
