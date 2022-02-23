import streamlit as st
from indicador.calculo_do_indicador import PontoDePivot


class App:
    def __init__(self) -> None:
        self.__indicador = PontoDePivot()

        self.__codigo = ''

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

        self.botao()

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    def botao(self):
        result = st.button('Calcular',
                           on_click=self.limpar)

        if result and len(self.codigo) > 0:
            self.resultado(self.codigo)

    def resultado(self, cod) -> None:
        st.markdown(f'* **Nome**: _{cod}_')

    def limpar(self):
        # self.__db.registrar(self.stock_name, self.__indicador.calcular_indicador(self.stock_name))
        self.codigo = self.stock_name
        st.session_state["stock"] = ""

    def acao(self):
        self.limpar()
