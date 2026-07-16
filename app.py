import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Mandarin Dashboard",
    page_icon="📚",
    layout="wide"
)

st.title("📚 My Mandarin Dashboard")
st.write("Welcome back! Ready to study today?")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cards Due", 24)

with col2:
    st.metric("Current Streak", "8 days")

with col3:
    st.metric("Words Learned", 156)

st.divider()

if st.button("🃏 Start Studying"):
    st.success("Study mode coming soon!")