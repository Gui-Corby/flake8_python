class FilaBase:
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual = ""

    def reseta_fila(self):
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1
