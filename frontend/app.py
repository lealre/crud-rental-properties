from http import HTTPStatus

import pandas as pd
import requests
import streamlit as st

from frontend.response import show_response_message

st.set_page_config(layout='wide')

st.title('Rental Property Inventory App')

with st.expander('Add a new property unit'):
    with st.form('new_item'):
        description = st.text_input('Description')
        number_bedrooms = st.selectbox(
            'Number Bedrooms',
            ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T6+'],
        )
        price = st.text_input('Price (€)')
        area = st.text_input('Area (m2)')
        location = st.text_input('Location')
        submit_button = st.form_submit_button('Add Property Unit')

        if submit_button:
            response = requests.post(
                'http://backend:8000/property/',
                json={
                    'description': description,
                    'number_bedrooms': number_bedrooms,
                    'price': price,
                    'area': area,
                    'location': location,
                },
            )

            show_response_message(response)


with st.expander('View All Listed Properties'):
    if st.button('Show All Properties'):
        response = requests.get('http://backend:8000/property/')
        if response.status_code == HTTPStatus.OK:
            properties = response.json()['properties']
            if properties:
                df = pd.DataFrame(properties)
                df = df[
                    [
                        'id',
                        'description',
                        'number_bedrooms',
                        'price',
                        'area',
                        'location',
                    ]
                ]

                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                st.error('There are no properties registered.')
        else:
            show_response_message(response)


with st.expander('Search for a Listed Property'):
    get_id = st.number_input('Property ID', min_value=1, format='%d')
    if st.button('Search Property'):
        response = requests.get(f'http://backend:8000/property/{get_id}')
        if response.status_code == HTTPStatus.OK:
            property = response.json()
            df = pd.DataFrame([property])

            df = df[
                [
                    'id',
                    'description',
                    'number_bedrooms',
                    'price',
                    'area',
                    'location',
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)


with st.expander('Delete a Listed Property'):
    delete_id = st.number_input(
        'Property ID to Delete', min_value=1, format='%d'
    )
    if st.button('Delete'):
        response = requests.delete(f'http://backend:8000/property/{delete_id}')
        show_response_message(response)


with st.expander('Update a Listed Property'):
    with st.form('update_property'):
        new_data = {}

        new_data['id'] = st.number_input(
            'Property ID', min_value=1, format='%d'
        )
        new_data['description'] = st.text_input('New Property Description')
        new_data['number_bedrooms'] = st.selectbox(
            'New Number of Bedrooms',
            ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T6+'],
        )
        new_data['price'] = st.number_input(
            'New Price',
            min_value=0.01,
            format='%f',
        )
        new_data['area'] = st.number_input('New Area')
        new_data['location'] = st.text_input('New Location')

        update_button = st.form_submit_button('Update Property')

        if update_button:
            update_data = {
                key: value for key, value in new_data.items() if value
            }

            if update_data:
                response = requests.patch(
                    f"http://backend:8000/property/{update_data.get('id')}",
                    json=update_data,
                )

                show_response_message(response)
            else:
                st.error(
                    'No changes were made as none of the fields were filled'
                )
