import streamlit as st

def header_home():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;margin-bottom:20px;margin-top:12px; ">
             <img src="{logo_url}" alt="VeriSnap AI logo" style="height: 88px;"/>
             <h1 style='text-align:center; margin:.35rem 0 0;'>VeriSnap AI</h1>
             <p style='text-align:center; margin:.25rem 0 0; color:#52635d;'>AI-assisted attendance for teachers and students</p>

        </div>
""",unsafe_allow_html=True)
    
def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' alt='VeriSnap AI logo' style='height:64px;' />
            <h2 style='text-align:left; margin:0;'>VeriSnap<br/>AI</h2>
        </div>
                """, unsafe_allow_html=True)
