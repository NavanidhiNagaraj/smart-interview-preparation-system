import streamlit as st

st.set_page_config(page_title="Smart Interview Preparation System")
st.title("Smart Interview Preparation System")
st.info("Starter scaffold. Implement modules incrementally.")

uploaded=st.file_uploader("Upload Resume",type=["pdf","docx","txt"])
role=st.selectbox("Job Role",["Software Engineer","Data Scientist","AI Engineer"])
if uploaded:
    st.success("Resume uploaded!")
    st.write("Next: integrate parser, ATS score, recommendations.")
