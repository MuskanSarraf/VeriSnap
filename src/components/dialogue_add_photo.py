
import streamlit as st
from PIL import Image
import hashlib


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    if 'processed_photo_hashes' not in st.session_state:
        st.session_state.processed_photo_hashes = set()

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    
    if st.session_state.photo_tab == 'camera':

        cam_photo = st.camera_input(
            'Take Snapshot',
            key='dialog_cam'
        )

        if cam_photo is not None:

            photo_bytes = cam_photo.getvalue()
            photo_hash = hashlib.sha256(photo_bytes).hexdigest()

            # Save the captured photo only once
            if photo_hash not in st.session_state.processed_photo_hashes:

                image = Image.open(cam_photo).convert('RGB').copy()

                st.session_state.attendance_images.append(image)
                st.session_state.processed_photo_hashes.add(photo_hash)

                st.success("Photo captured and saved successfully!")

            # Display the captured photo
            st.subheader("Captured Photo Preview")
            st.image(
                cam_photo,
                caption="Captured Photo",
                width=300
            )

    if st.session_state.photo_tab == 'upload':

        uploaded_files = st.file_uploader(
            'Choose image files',
            type=['jpg', 'png', 'jpeg'],
            accept_multiple_files=True,
            key='dialog_upload'
        )

        if uploaded_files:
            for f in uploaded_files:
                photo_bytes = f.getvalue()
                photo_hash = hashlib.sha256(photo_bytes).hexdigest()

                if photo_hash not in st.session_state.processed_photo_hashes:
                    image = Image.open(f).copy()
                    st.session_state.attendance_images.append(image)
                    st.session_state.processed_photo_hashes.add(photo_hash)

            st.subheader('Uploaded Photo Preview')

            preview_cols = st.columns(3)

            for idx, f in enumerate(uploaded_files):
                with preview_cols[idx % 3]:
                    st.image(
                        f,
                        width='stretch',
                        caption=f'Photo {idx + 1}'
                    )

    st.divider()

    st.caption(
        f"Total photos added: {len(st.session_state.attendance_images)}"
    )

    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
