import library.process
import library.output
import library.input

import streamlit as st
import pandas as pd

def main():
    students = pd.read_csv(r'data\Sample_Student_Data_File.csv')
    p = library.process.Process(students)

    p.generate_teams()

    o = library.output.Output(p.teams)

    o.display_chart()

    with st.form(key='name_form', clear_on_submit=False):
            name_input = st.text_input(label='Enter name', placeholder='SURNAME, Firstname')

            submitted = st.form_submit_button("Submit")

            if submitted:
                if o.student_name_inquiry(name_input):
                    st.write("Found")
                else:
                    st.write("Please try again, team not found.")
    
    with st.form(key='id_form', clear_on_submit=False):
            id_input = st.text_input(label='Enter student ID', placeholder='12345678')

            submitted = st.form_submit_button("Submit")

            if submitted:
                if o.student_name_inquiry(id_input):
                    st.write("Found")
                else:
                    st.write("Please try again, team not found.")

    
    st.subheader('Teaming Up performance by Team Average - Graph')
    df = o.display_chart()
    st.line_chart(df)


if __name__ == "__main__":
    main()
