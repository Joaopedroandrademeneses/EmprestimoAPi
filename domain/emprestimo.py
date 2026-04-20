class Emprestimo:
    def __init__(id:int,brinquedo_id:int,datas: str,multa: float,crianca_id:int =[],status:bool=True):
        if len(crianca_id)>2:
            raise ValueError("Numero de emprestimos maximo atingido.")
        def multapordia(dias_atraso:int)->float:
            if dias_atraso>=0:
                raise ValueError("Dias de atraso não pode ser negativo.")
            else:
                for i in dias_atraso:
                    multa++2
            return 0.0

