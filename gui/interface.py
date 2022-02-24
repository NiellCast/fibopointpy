import streamlit as st
from indicador.calculo_do_indicador import PontoDePivot
from database.db import BancoDeDados
from os import getenv
from dotenv import load_dotenv


class App:
    load_dotenv()

    def __init__(self) -> None:
        self.__indicador = PontoDePivot()
        self.__db = BancoDeDados(getenv('DATABASE'))

        self.config = st.set_page_config(
            page_title='Ponto de Pivot',
            page_icon=':chart_with_upwards_trend:',
            layout="centered"
        )
        self.titulo = st.title('Ponto de Pivot')
        self.caption = st.caption('Esta ferramenta utiliza o método LeandroStormer.')

        self.stock_name = st.text_input(
            'CÓDIGO DA AÇÃO:',
            value='',
            help='Não são aceitas ações fracionárias.',
            placeholder='EX: VALE3',
            key='stock'
        ).strip().upper()

        self.criar_botao()

    def criar_botao(self) -> None:
        result = st.button('Calcular',
                           on_click=self.receber_dados)

        if result:
            if len(self.stock_name) > 0 and 'F' not in self.stock_name[-1]:
                self.mostrar_resultado()

    def receber_dados(self) -> None:
        if len(self.stock_name) > 0 and 'F' not in self.stock_name[-1]:
            dados = self.__indicador.calcular_indicador(self.stock_name)

            if dados:
                self.__db.salvar(self.stock_name, dados['resistencia_4'], dados['resistencia_3'], dados['resistencia_2'],
                                 dados['resistencia_1'], dados['pivot_point'], dados['suporte_1'], dados['suporte_2'],
                                 dados['suporte_3'], dados['suporte_4'])

                st.session_state["stock"] = ""

    @staticmethod
    def escrever_na_tela(item: str, valor: str) -> None:
        st.markdown(f'* **{item}**: _{valor}_')

    def mostrar_resultado(self) -> None:
        self.escrever_na_tela('Nome', self.__db.listar()[0])
        self.escrever_na_tela('Resistência 4', self.__db.listar()[1])
        self.escrever_na_tela('Resistência 3', self.__db.listar()[2])
        self.escrever_na_tela('Resistência 2', self.__db.listar()[3])
        self.escrever_na_tela('Resistência 1', self.__db.listar()[4])
        self.escrever_na_tela('Ponto de Pivot', self.__db.listar()[5])
        self.escrever_na_tela('Suporte 1', self.__db.listar()[6])
        self.escrever_na_tela('Suporte 2', self.__db.listar()[7])
        self.escrever_na_tela('Suporte 3', self.__db.listar()[8])
        self.escrever_na_tela('Suporte 4', self.__db.listar()[9])

        self.__db.remover(self.__db.listar()[0])
