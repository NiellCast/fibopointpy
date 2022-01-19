from investpy import get_stocks


class Verificacao:
    @staticmethod
    def verificar(ativo: str) -> bool:
        """
        :param ativo: Recebe o código de uma ação.
        :return: Retorna True se a ação recebida existir no pacote investpy.
        """
        return True if ativo in [x for x in get_stocks('brazil')['symbol']] else False
