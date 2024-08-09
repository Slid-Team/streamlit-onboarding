"""
Sample script to learn streamlit
"""

import streamlit as st

def main():
    """
    Maim function
    """

    st.set_page_config(page_title="Multipage App", page_icon="👋")

    st.title("Bebridge Streamlit Onboarding Sample App")
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        This is the homepage of your multipage app.
        Select a page from the sidebar to see other pages.
        """
    )

    


if __name__ == "__main__":
    main()
