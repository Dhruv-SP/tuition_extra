#a calculator streamlit app 

import streamlit as st

st.title(body="calculator", anchor="top")

#st.text_area("Enter your text here")
num_1 = st.text_input("Enter number 1")
num_2 = st.text_input("Enter number 2")
num_3 = None

col1, col2, col3 = st.columns([3,3,1])

with col1:
    if st.button("Add"):
        if num_1 == '' or num_2 == '': 
            st.write("Please enter both numbers")
        else:
            st.write("Sum is: ", int(num_1) + int(num_2))

with col2:
    if st.button("Subtract"):
        st.write("Difference is: ", int(num_1) - int(num_2))

with col3:
    if st.button("Multiply"):
        st.write("Product is: ", int(num_1) * int(num_2))

ascii_input = st.text_input("Enter ASCII value")
if st.button("Convert to Character"):
    if ascii_input:
        try:
            char = chr(int(ascii_input))
            st.write(f"Character: {char}")
        except ValueError:
            st.write("Please enter a valid ASCII value")
