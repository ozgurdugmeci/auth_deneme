import streamlit as st
'Hop'
if st.experimental_user.is_logged_in:
    st.write(st.experimental_user)

'''if not st.experimental_user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!")

#user =st.experimental_user
#user

#st.stop()'''
