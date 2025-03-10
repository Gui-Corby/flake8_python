# flake8: noqa: F401

from fila_normal import fila_normal
from fila_prioritaria import FilaPrioritaria

# fila_teste = fila_normal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# print(fila_teste.chamar_cliente(5))
# print(fila_teste.chamar_cliente(3))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(7))
print(fila_teste_2.chama_cliente(4))
print(fila_teste_2.estatistica('10/01/2025', 198, 'detail'))
