import streamlit as st


def set_page_config(title: str) -> None:
    """
    :return: Configure the application.
    """

    st.set_page_config(
        page_title=title,
        page_icon=':chart_with_upwards_trend:',
        layout="centered"
    )
