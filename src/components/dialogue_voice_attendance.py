import streamlit as st
import pandas as pd
from datetime import datetime

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from src.components.dialogue_attendance_results import show_attendance_result


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):

    st.write(
        "Record audio of students saying 'I am present'. "
        "The AI will identify enrolled students from their voice."
    )

    # Audio input with fixed key
    audio_data = st.audio_input(
        "Record classroom audio",
        key="voice_attendance_audio"
    )

    # Debug (remove later)
    if audio_data is not None:
        st.success("Audio recorded successfully.")

    if st.button(
        "Analyze Audio",
        width="stretch",
        type="primary",
        key="analyze_voice_btn"
    ):

        # Retrieve from session state
        audio_data = st.session_state.get("voice_attendance_audio")

        if audio_data is None:
            st.warning("Please record classroom audio first.")
            return

        with st.spinner("Processing audio..."):

            enrolled_res = (
                supabase
                .table("subjects_students")
                .select("*, students(*)")
                .eq("subject_id", selected_subject_id)
                .execute()
            )

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning("No students enrolled in this course.")
                return

            candidates_dict = {
                s["students"]["student_id"]: s["students"]["voice_embedding"]
                for s in enrolled_students
                if s["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.error(
                    "No enrolled students have registered voice profiles."
                )
                return

            try:
                audio_bytes = audio_data.read()

                if not audio_bytes:
                    st.error("Recorded audio is empty.")
                    return

            except Exception as e:
                st.error(f"Audio read failed: {e}")
                return

            detected_scores = process_bulk_audio(
                audio_bytes,
                candidates_dict
            )

            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S"
            )

            for node in enrolled_students:

                student = node["students"]

                score = detected_scores.get(
                    student["student_id"],
                    0.0
                )

                is_present = score > 0

                results.append({
                    "Name": student["name"],
                    "ID": student["student_id"],
                    "Source": round(score, 4) if is_present else "-",
                    "Status": (
                        "✅ Present"
                        if is_present
                        else "❌ Absent"
                    )
                })

                # Using your database column name
                attendance_to_log.append({
                    "student_id": student["student_id"],
                    "subject_id": selected_subject_id,
                    "timestamp": current_timestamp,
                    "id_present": bool(is_present)
                })

            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log
            )

            st.rerun()

    if st.session_state.get("voice_attendance_results"):

        st.divider()

        df_results, logs = (
            st.session_state.voice_attendance_results
        )

        show_attendance_result(df_results, logs)