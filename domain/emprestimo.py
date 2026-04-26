class Emprestimo:
    def __init__(self, id: int, brinquedo_id: int, datas: str, multa: float, crianca_id: list = [], status: bool = True):
        if len(crianca_id) > 2:
            raise ValueError("Numero de emprestimos maximo atingido.")
        self.id = id
        self.brinquedo_id = brinquedo_id
        self.datas = datas
        self.multa = multa
        self.crianca_id = crianca_id
        self.status = status

    def multapordia(self, dias_atraso: int) -> float:
        if dias_atraso <= 0:
            raise ValueError("Dias de atraso não pode ser zero ou negativo.")
        multa = 0.0
        for _ in range(dias_atraso):
            multa += 2
        return multa