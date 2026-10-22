import pytest

from main import calcular_area_triangulo 

    
def test_area_triangulo():
    #resultado obtenido (real)
    actual_result =  calcular_area_triangulo(13.1, 3.85)

    #asserts (estamos asegurando o verificando que el resultado obtenido es igual al resultado esperado)
    assert actual_result == pytest.approx(19.5, 0.001)  # resultado esperado (esperado)