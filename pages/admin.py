import streamlit as st
'Hello admin'
st.header(f"Logged in with {st.experimental_user.email}")
st.json(st.experimental_user)

if st.button("🔓 Logout"):
 st.logout()

