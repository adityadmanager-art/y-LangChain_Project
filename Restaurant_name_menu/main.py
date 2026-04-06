import streamlit as st
import Restaurant_name_menu.langchain_helper as langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian", "Mexican", "Arabic", "Italian", "American"))


    
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for items in menu_items:
        st.write("-", items)
