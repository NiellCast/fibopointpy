__author__ = "Daniell Castelo Branco Ciriaco"
__email__ = "niellcast.contato@outlook.com"

import streamlit as st
from time import sleep
from src.database.db import Database
from src.config.page_config import set_page_config
from src.indicador.pivot_point import PivotPoint


def run() -> None:
    set_page_config('Fibo Point')
    data = Database('data.db')

    menu = st.sidebar.selectbox(
        'SELECIONAR IDIOMA - SELECT LANGUAGE',
        ['', 'Português', 'English']
    )

    if menu == 'Português':
        st.title('Ponto de Pivot')
        st.caption('Esta ferramenta utiliza o método LeandroStormer.')

        stocks = [i[0] for i in data.read()]
        stocks.insert(0, ' ')

        stock = st.selectbox(
            label='Escolha uma ação.',
            options=stocks,
            help='Não são aceitas ações fracionárias.'
        )

        if stock != ' ':
            with st.spinner('Calculando...'):
                result = PivotPoint.calculate(stock)
                sleep(3)

                col9, col10, col11, col12, col13 = st.columns(5)

                with col11:
                    st.metric(label='Ponto de Pivot',
                              value=result["pivot_point"])

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(label=f'Resistência 1',
                              value=result[f"resistencia_1"])

                with col2:
                    st.metric(label=f'Resistência 2',
                              value=result[f"resistencia_2"])

                with col3:
                    st.metric(label=f'Resistência 3',
                              value=result[f"resistencia_3"])

                with col4:
                    st.metric(label=f'Resistência 4',
                              value=result[f"resistencia_4"])

                col5, col6, col7, col8 = st.columns(4)

                with col5:
                    st.metric(label=f'Suporte 1',
                              value=result[f"suporte_1"])

                with col6:
                    st.metric(label=f'Suporte 2',
                              value=result[f"suporte_2"])

                with col7:
                    st.metric(label=f'Suporte 3',
                              value=result[f"suporte_2"])

                with col8:
                    st.metric(label=f'Suporte 4',
                              value=result[f"suporte_4"])

    elif menu == 'English':
        st.title('Coming Soon')


if __name__ == '__main__':
    run()
