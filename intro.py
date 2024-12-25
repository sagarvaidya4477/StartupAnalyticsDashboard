import time
import streamlit as st
# import pandas as pd
#
# st.set_page_config(layout = "wide", page_title = "Lecture")
#
# st.title("Sagar's Streamlit app")
# st.header("Header text")
# st.subheader("First subheading")
#
# st.write("This is the text line using write function")
#
# st.code("""
# def show_date(name):
#     print("Hi", name)
# """)
#
# df = pd.DataFrame(
#     [['Andhra Pradesh', 'Adilabad', 19.284513950073435,
#         78.81321233480176, 2741239],
#        ['Andhra Pradesh', 'Anantapur', 14.312065561843148,
#         77.4601584478577, 4081148]]
# )
# st.dataframe(df)
#
# st.json(df)
#
# col1, col2 = st.columns(2)
# with col1:
#     st.image("Superstore_bg.jpg")
# with col2:
#     st.dataframe(df)
#
# # st.video()
# # st.audio()
#
# st.metric("Total Cases", "250", "-50%", help = "These are total cases of Corona Virus pandemic")
#
# st.markdown("""
# ### Python Frameworks
# - Tkinter
# - Dash
# - Flask
# - Streamlit
# """)
#
# st.error("Some Error Occurred")
# st.success("Successful")
# st.info("Information")
# st.warning("Warn")
#
# st.sidebar.title("This is a sidebar")
#
# st.button("OKAY")
#
# st.sidebar.button("Login")
#
# st.selectbox("Select an option", ["Option 1", "Option 2", "Option"])
#
# st.checkbox("Checkbox 1")
#
# st.slider("My slider", 0, 100)
#
# st.text_input("Enter your name")
#
# st.number_input("Enter age", min_value=0.0, max_value=100.5, step=0.5)
#
# st.text_area("address")
#
# st.date_input("DOB")
#
# st.file_uploader("Upload resume")
#
# st.radio("Gender", ["Male", "Female"])

st.title("Login Form")

email = st.text_input("Enter Email")
password = st.text_input("Password")

login_btn = st.button("Login")

if login_btn:
    if email == "test@gmail.com" and password == "9898":
        st.balloons()
        st.snow()
        st.success("Login Successful")
    else:
        st.error("Invalid")
#
# a = st.progress(0)
#
# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
#
# for percent_complete in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(1)
# my_bar.empty()
#
# st.button("Rerun")
#
#
# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

