import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.title("Rental Property Inventory App")

def show_response_message(response):
    if response.status_code == 200:
        st.success("Operation completed successfully!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Unknown error. Unable to decode the response.")


with st.expander("Add a new property unit"):
    with st.form("new_item"):
        description = st.text_input("Description")
        house_type = st.selectbox(
            "House Type",
            ["T0", "T1", "T2", "T3", "T4", "T5+"],
        )
        price = st.text_input("Price (€)")
        area = st.text_input("Area (m2)")
        location = st.text_input("Location")
        submit_button = st.form_submit_button("Add Property Unit")

        if submit_button:
            response = requests.post(
                "http://backend:8000/properties/",
                json={
                    "description": description,
                    "house_type" : house_type,
                    "price": price,
                    "area": area,
                    "location": location
                },
            )
            show_response_message(response)


with st.expander("View All Listed Properties"):
    if st.button("Show All Properties"):
        response = requests.get("http://backend:8000/properties/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "id",
                    "description",
                    "house_type",
                    "price",
                    "area",
                    "location"
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)


with st.expander("Search for a Listed Property"):
    get_id = st.number_input("Property ID", min_value=1, format="%d")
    if st.button("Search Property"):
        response = requests.get(f"http://backend:8000/properties/{get_id}")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

            df = df[
                [
                    "id",
                    "description",
                    "house_type",
                    "price",
                    "area",
                    "location"
                ]
            ]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)


with st.expander("Delete a Listed Property"):
    delete_id = st.number_input("Property ID to Delete", min_value=1, format="%d")
    if st.button("Delete"):
        response = requests.delete(f"http://backend:8000/properties/{delete_id}")
        show_response_message(response)


with st.expander("Update a Listed Property"):
    with st.form("update_product"):
        update_id = st.number_input("Property ID", min_value=1, format="%d")
        new_description = st.text_input("New Property Description")
        new_house_type = st.selectbox(
            "New House Type",
            ["T0", "T1", "T2", "T3", "T4", "T5+"],
        )
        new_price = st.number_input(
            "New Price",
            min_value=0.01,
            format="%f",
        )
        new_area = st.text_area("New Area")
        new_location = st.text_input("New Location")

        update_button = st.form_submit_button("Update Property")

        if update_button:
            update_data = {}
            if new_description:
                update_data["description"] = new_description
            if new_house_type:
                update_data["house_type"] = new_house_type
            if new_price > 0:
                update_data["price"] = new_price
            if new_area:
                update_data["area"] = new_area
            if new_location:
                update_data["location"] = new_location

            if update_data:
                response = requests.put(
                    f"http://backend:8000/properties/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("No changes were made as none of the fields were filled")