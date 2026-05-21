import pytest
from src.calculadora.operacoes import (somar, subtrair, multiplicar, dividir, potencia, raiz_quadrada)

def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -4) == -5 

def test_multiplicar():
    assert multiplicar(3, 7) == 21

def test_subtrair_positivos():
    assert subtrair(10, 4) == 6

def test_subtrair_negativos():
    assert subtrair(-5, -3) == -2

def test_potencia_quadrado():
    assert potencia(3, 2) == 9

def test_potencia_expoente_zero():
    assert potencia(5, 0) == 1

def test_potencia_expoente_negativo ():
    assert potencia(2, -3) == pytest.approx(0.125)

def test_raiz_quadrada_valida():
    assert raiz_quadrada(16) == 4

def test_raiz_quadrada_numero_negativo_levanta_excecao():
    with pytest.raises(ValueError):
        raiz_quadrada(-9)

def test_dividir_por_zero_levanta_excecao():
    with pytest.raises(ValueError):
        dividir(6, 0)

def test_dividir_positivos_resultado_inteiro():
    assert dividir(8, 2) == 4