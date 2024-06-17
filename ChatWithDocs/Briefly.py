import streamlit as st

def main(): 
    st.set_page_config(page_title="Chat With your PDF's", page_icon=":books:")
    st.header("Chat With your Documents :books: ")
    st.text_input("Ask a Question !!")

    with st.sidebar: 
        st.subheader("Your Documents")
        st.file_uploader("Click on Upload to upload your files here")
        st.button("Upload")


if __name__ == '__main__':
    main()
