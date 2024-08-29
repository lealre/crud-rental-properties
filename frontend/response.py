from http import HTTPStatus

import streamlit as st


def show_response_message(response):
    if response.status_code in {HTTPStatus.OK, HTTPStatus.CREATED}:
        st.success('Operation completed successfully!')
    else:
        try:
            data = response.json()
            if 'detail' in data:
                if isinstance(data['detail'], list):
                    errors = '\n'.join([
                        error['msg'] for error in data['detail']
                    ])
                    st.error(f'Erro: {errors}')
                else:
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error('Unknown error. Unable to decode the response.')
