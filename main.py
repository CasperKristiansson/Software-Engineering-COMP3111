import library.process
import library.output
import library.input

import streamlit as st


def main():
    st.set_page_config(layout="wide", page_title="Team Formation", page_icon=":robot_face:")

    i = library.input.Input()

    col1, col2, col3 = st.columns([2, 5, 2])

    with col2:
        uploaded_file = st.file_uploader("Please Upload File", type=None, accept_multiple_files=False, key=None, help=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

        if st.button("Generate", disabled=not uploaded_file):
            p = library.process.Process(r'data\Sample_Student_Data_File.csv')
            p.process_data()
            p.create_output()

            o = library.output.Output(p.output)
            o.render_output()

    if uploaded_file:
        i.render_data(uploaded_file)
        st.table(i.students)

    # students = pd.read_csv(r'data\Sample_Student_Data_File.csv')
    # p = library.process.Process(students)

    # p.generate_teams()

    # o = library.output.Output(p.teams)

    # o.display_chart()

    # with st.form(key='name_form', clear_on_submit=False):
    #     name_input = st.text_input(label='Enter name', placeholder='SURNAME, Firstname')
    #     submitted = st.form_submit_button("Submit")

    #     if submitted:
    #         if o.student_name_inquiry(name_input):
    #             st.write("Found")
    #         else:
    #             st.write("Please try again, team not found.")

    # with st.form(key='id_form', clear_on_submit=False):
    #     id_input = st.text_input(label='Enter student ID', placeholder='12345678')
    #     submitted = st.form_submit_button("Submit")

    #     if submitted:
    #         if o.student_name_inquiry(id_input):
    #             st.write("Found")
    #         else:
    #             st.write("Please try again, team not found.")

    # st.subheader('Teaming Up performance by Team Average - Graph')
    # df = o.display_chart()
    # st.line_chart(df)


if __name__ == "__main__":
    main()
