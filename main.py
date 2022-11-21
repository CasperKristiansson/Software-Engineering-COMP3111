import library.process
import library.output
import library.input

import streamlit as st


def main():
    st.set_page_config(layout="wide", page_title="Team Formation", page_icon=":robot_face:")
    st.markdown("<h1 style='text-align: center'>Team Formation</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center'>Input</h2>", unsafe_allow_html=True)
    i = library.input.Input()

    _, upload_column, _ = st.columns([2, 5, 2])
    with upload_column:
        uploaded_file = st.file_uploader("Please Upload File", type=None, accept_multiple_files=False, key=None, help=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    if uploaded_file:
        with st.expander("View Table", expanded=True):
            i.render_data(uploaded_file)
            st.table(i.df)

    st.markdown("<h2 style='text-align: center'>Output</h2>", unsafe_allow_html=True)

    _, button_column, _ = st.columns([41, 9, 40])
    with button_column:
        button = st.button("Generate Teams", disabled=not uploaded_file)
        find_team_button = st.button("Find your team", disabled=not button)

        if not st.session_state.get('button'):
            st.session_state['button'] = button  # Saved the state of button

        if not st.session_state.get('find_team_button'):
            st.session_state['find_team_button'] = find_team_button  # Saved the state find_team_button

    _, chart_column, _ = st.columns([2, 5, 2])
    with chart_column:
        if st.session_state['button']:
            p = library.process.Process(i.students)

            with st.spinner("Generating Teams..."):
                p.generate_teams()

            o = library.output.Output(p.teams)
            df = o.display_chart()

            st.subheader('Teaming Up performance by Team Average - Graph')
            st.line_chart(df)

            if st.session_state['find_team_button']:
                st.subheader('Find your team: ')

                with st.form(key='name_form', clear_on_submit=False):
                    name_input = st.text_input(label='Enter name', placeholder='SURNAME, Firstname')
                    if st.form_submit_button("Submit"):
                        df = o.student_name_inquiry(name_input)

                        if df is None:
                            st.write("Please try again, team not found.")
                        else:
                            st.table(df)

                with st.form(key='id_form', clear_on_submit=False):
                    id_input = st.text_input(label='Enter student ID', placeholder='12345678')
                    if st.form_submit_button("Submit"):
                        df = o.student_id_inquiry(id_input)

                        if df is None:
                            st.write("Please try again, team not found.")
                        else:
                            st.table(df)


if __name__ == "__main__":
    main()
