import streamlit as st

st.title("📚 My Mandarin Dashboard")

st.write("Welcome back!")

st.metric("Cards Due", 24)
st.metric("Current Streak", "8 days")

if st.button("Start Studying"):
    st.success("Let's learn some Mandarin!")