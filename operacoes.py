import math

def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a diferença de dois números."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(base: float, exp: float) -> float:
    return base ** exp

def raiz_quadrada(numero: float) -> float:
    if numero < 0:
        raise ValueError("Nao existe raiz real de numero negativo")
    return math.sqrt(numero) 