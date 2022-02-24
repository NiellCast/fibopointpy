from sqlite3 import connect


class BancoDeDados:
    def __init__(self, db: str) -> None:
        self.conexao = connect(db, check_same_thread=False)
        self.cursor = self.conexao.cursor()

    def salvar(self, codigo: str, resistencia4: str, resistencia3: str, resistencia2: str, resistencia1: str, pp: str,
               suporte1: str, suporte2: str, suporte3: str, suporte4: str) -> None:

        self.cursor.execute(
            'INSERT OR IGNORE INTO temp (codigo, resistencia4, resistencia3, resistencia2, resistencia1, pp,'
            ' suporte1, suporte2, suporte3, suporte4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',

            (codigo, resistencia4, resistencia3, resistencia2, resistencia1, pp, suporte1,
             suporte2, suporte3, suporte4)

        )
        self.conexao.commit()

    def remover(self, codigo: str) -> None:
        self.cursor.execute(
            'DELETE FROM temp WHERE codigo=?',
            (codigo,)
        )
        self.conexao.commit()

    def listar(self) -> str:
        self.cursor.execute('SELECT * FROM temp')

        return self.cursor.fetchall()[0]

    def fechar_conexao(self) -> None:
        self.conexao.close()
        self.cursor.close()
