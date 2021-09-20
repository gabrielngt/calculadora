import abc
from typing import AbstractSet
from unittest import TestCase, main, result


class Calculadora(object):
    def calcular(self, valor, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor, valor2)
            return resultado


class OperacaoFabrica(object):

    def criar(self, operador):
        if operador == "soma":
            return Soma()
        elif operador == "subtracao":
            return Subtracao()
        elif operador == "divisao":
            return Divisao()
        elif operador == "multiplicacao":
            return Multiplicacao()


class Operacao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, valor, valor2):
        pass


class Soma(Operacao):
    def executar(self, valor, valor2):
        resultado = valor + valor2
        return resultado


class Subtracao(Operacao):
    def executar(self, valor, valor2):
        resultado = valor - valor2
        return resultado


class Multiplicacao(Operacao):
    def executar(self, valor, valor2):
        resultado = valor * valor2
        return resultado


class Divisao(Operacao):
    def executar(self, valor, valor2):
        resultado = valor / valor2
        return resultado


class Teste(TestCase):

    def testar_soma(self):
        calculador = Calculadora()
        result = calculador.calcular(15, 10, 'soma')
        print(result)
        self.assertEqual(result, 25)

    def testar_subtracao(self):
        calculador = Calculadora()
        result = calculador.calcular(15, 10, 'subtracao')
        print(result)
        self.assertEqual(result, 5)

    def testar_multipicacao(self):
        calculador = Calculadora()
        result = calculador.calcular(15, 10, 'multiplicacao')
        print(result)
        self.assertEqual(result, 150)
        
    def testar_divisao(self):
        calculador = Calculadora()
        result = calculador.calcular(15, 10, 'divisao')
        print(result)
        self.assertEqual(result, 1.5)



if __name__ == "__main__":

    main()
