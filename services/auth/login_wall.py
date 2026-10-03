import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.markdown(
    "<h1 style='font-size:38px;'>🏋️ RepWise real-time GYM Coach</h1>",
    unsafe_allow_html=True)

    st.markdown(
        "<h2 style='font-size:22px;'>Welcome! Please enter a username to start.</h2>",
        unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name(unique)", placeholder='unique name eg. manku')
        submit_button = st.form_submit_button("Start Session", width = "stretch")

    if submit_button:
        if not username:
            st.error("Please enter your name!")
            return False

        st.session_state["username"] = username
        st.session_state["user_id"] = "1"

        st.rerun()

    return False