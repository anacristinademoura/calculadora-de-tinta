from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Informe a largura do cômodo: '),
    input('Informe a profundidade do cômodo: ')
)

print(
    'A área das paredes é ',
    calc.calcular_area_paredes(
        comodo
    )
)

print(
    'A área das teto é ',
    calc.calcular_area_teto(
        comodo
    )
)

print(
    'A litragem necessária é ',
    calc.calcular_litragem_necessaria()
)