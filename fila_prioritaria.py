# flake8: noqa: E501
from fila_base import FilaBase
class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{self.codigo}'

 

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str):
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(self.clientes_atendidos)

        return estatistica
