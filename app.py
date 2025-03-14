import streamlit as st
'Hop'
#st.login("google")
####-------------------------------------------------
st.set_page_config(
    page_title="page_title",
    page_icon="✨",
    initial_sidebar_state="collapsed",
)

# Define app pages
landing_page = st.Page("./app/landing.py", title="Landing", icon=":material/home:")
app_page = st.Page("./app/app.py", title="App", icon=":material/play_arrow:")
admin_page = st.Page(
    "./app/admin.py", title="Admin", icon=":material/admin_panel_settings:"
)

# Enables switch_page behaviour
if not st.experimental_user.is_logged_in:
    pg = st.navigation(
        [landing_page],
        position="hidden",
    )
elif st.experimental_user.email == st.secrets["admin_email"]:
    pg = st.navigation(
        [app_page, admin_page],
    )
else:
    pg = st.navigation(
        [app_page],
        position="hidden",
    )

# Head to first page of navigation
pg.run()


'''if not st.experimental_user.is_logged_in:
    if st.button("Log in"):
        st.login("google")
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!")'''

#user =st.experimental_user
#user

#st.stop()
