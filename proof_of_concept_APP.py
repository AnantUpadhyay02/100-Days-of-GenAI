#here we are using streamlit library for POC app 
import streamlit as st
from langchain_helper import generate_business_name
st.title("Business Name Generator")

business = st.sidebar.selectbox("pick a business",("Chinese Restaurant", "Gas Station", "Car Dealership", "Clothing Store", "Bakery", "Pharmacy", "Gym", "Coffee Shop", "Law Firm", "Consulting Agency", "Florist", "Real Estate Agency", "Bookstore", "IT Services Company", "Landscaping Service", "Automotive Repair Shop", "Dental Clinic", "Construction Company", "Online Retailer", "Event Planning Service"))




if business:
    response = generate_business_name(business)
    st.header(response['business_name'])
    products = response['products']
    st.write("**Products that we are selling**")
    for item in products:
        st.write("*",item)