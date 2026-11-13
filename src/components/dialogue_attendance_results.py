import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


from src.database.db import create_attendance

def show_attendance_result(df, logs):
    present_count = sum(bool(log.get('is_present')) for log in logs)
    absent_count = len(logs) - present_count
    st.write(f'{present_count} present · {absent_count} absent')
    if present_count == 0:
        st.warning('No enrolled students were recognized. Check the photos and subject, or confirm only if everyone should be marked absent.')
    else:
        st.caption('Review each student and the photo source before saving this attendance session.')
    st.dataframe(df, hide_index=True, width='stretch')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Save attendance', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Attendance could not be saved. Check your connection and try again; your reviewed results are still available.')



@st.dialog("Review attendance")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)

