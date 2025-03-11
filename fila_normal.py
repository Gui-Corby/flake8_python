from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gerar_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gerar_senha_atual()
        self.fila.append(self.senha_atual)

    def chamar_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual:{cliente_atual}, dirija-se ao caixa: {caixa}')
