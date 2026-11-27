#Login page 
import streamlit as st
st.title("Welcome To Login Page for intrenship")    #main headinf og the logoin page

age=st.number_input(
    "Age",
    min_value=20,
    max_value=40
)
batch_year=st.number_input(
    "Graduated Year",
    min_value=2026,
    max_value=2028
)

#selection
select=st.selectbox(
    "Qualification",
    ["BE","BEd","Master","MTech","BTech"]
)

select=st.selectbox(
    "Role",
    ["AIENG","DEVOPS","CLOUD","PYTHON DEV","GENAI","ML","WEB DEV","FULL STACK"]
)
#Resume uploading 
st.header("Upload Resume")
resume=st.file_uploader(
    "choose your resume",
    type=["pdf","jpg","files"]
)
#it show in format of box type 
user_name=st.text_input("Username")
user_password=st.text_input("Password")

#columns lest and right side
col1,col2=st.columns(2)
with col1:
    st.write("Creat Account")
with col2:
    st.write("Forgot Password")

if st.button("Login"):
    if user_name=="shruthisha" and user_password=="shru":
        st.write("login successfully")
    else:
        st.write("invalid")

