#STUDENT MANAGEMENT LOGIN PAGE
import streamlit as st

#page configuration in .com type in browser
st.set_page_config(
    page_title="management app.com",
    page_icon="🌐")


#title of the page
st.title("Student Management Login")

#corner of the student details
with st.container(border=True):
    st.header("Student Details")

    name=st.text_input(
        "Enter student name")

    age=st.number_input(
        "Age",
        min_value=0,
        max_value=50
    )
    
    #father name
    father_name=st.text_input(
        "Enter Father Name")
    
    #mother name
    mother_name=st.text_input(
        "Enter Mother Name")

    #place
    place=st.selectbox(
        "place",
        ["shivamogga","Bng","Mysuru","Chikkmagaluru","Tumkuru","Dharwada"]
    )

with st.container(border=True):
    st.header("Study Details")
    #college name
    college=st.text_input("Enter College Name")

    #college place
    college_place=st.text_input("Enter College Place")

    #college specialisation
    branch=st.selectbox(
        "Branch",
        ["AIML","CSE","DATA SCI","BUSINESS"]
    )

    resume=st.file_uploader(
        "Resume here",
        type=["pdf","jpf"],
        max_upload_size=5
    )
    
    college_info=st.text_area(
        "Descibe College Info",
        placeholder="Type here...."
    )
with st.container():
    st.header("Login Form")

    #user name
    user_name=st.text_input(
       "Enter User Name")

    #password    
    password=st.text_input(
    "Enter Password",
    type="password"
   )

    col1,col2=st.columns(2)
    with col1:
        st.write("Create account")

    with col2:
        st.write("Forgot password")

#side bar settings
with st.sidebar:
    st.header("Side Bar")
    st.subheader("Subject details")

    #select option
    kannada=st.checkbox("Kannda")
    English=st.checkbox("English")
    Hindi=st.checkbox("Hindi")
    Python=st.checkbox("Python")
    Dsa=st.checkbox("Dsa")
    Aiml=st.checkbox("AIML")
    Rag=st.checkbox("Rag")
    Deployment=st.checkbox("Deployment")
    Api=st.checkbox("Api")

    #settings
    st.subheader("Mobile settings ♻️")
    settings=st.selectbox(
        "Network Connection",
        ["WIFI","Mobile Data"]
    )
    
    st.subheader("Notification Settings")
    notification=st.toggle("notification seetings")
    if notification:
        st.write("Enable notification")
    else:
        st.write("not enable")
    
    st.subheader("Education Level")
    education=st.radio(
        "select current education",
        ["UG","PG","School"]
    )

if st.button("◀️Submit"):
    if not name or not father_name or not mother_name or not place:
        st.warning("please submit the student details")
    if age==0:
        st.warning("age is not be zero")
    if not college_place or not branch or not college:
        st.warning("please submit the study details")
    if not user_name or not password:
        st.warning("please submit the login credential details")
    if resume is None:
        st.warning("please upload resume⚠️")
    else:
        st.write("Thankyou for submiting the all details💐💐!")






    
    
    
    
    