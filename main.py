# import library.process
# import library.output
import library.input

import streamlit as st


def main():
    i = library.input.Input()


    uploaded_file = st.file_uploader("Please Upload File", type=None, accept_multiple_files=False, key=None, help=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    if uploaded_file is not None:
        i.render_data(uploaded_file)
        i.file_is_uploaded = True
        st.button("Generate", disabled = not i.file_is_uploaded)
        st.table(i.students)
        
    else:
        i.file_is_uploaded = False
        st.button("Generate", disabled = not i.file_is_uploaded)



if __name__ == "__main__":
    main()
