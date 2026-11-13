import streamlit as st
from html import escape

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <section style="background:#fff; padding:1.25rem; border-radius:12px; border:1px solid #d9e0dc; margin-bottom:1rem;">
        <h3 style="margin:0; color:#202c29; font-size:1.2rem">{escape(str(name))}</h3>
        <p style="color:#52635d; margin:.65rem 0 1rem;">Code: <strong>{escape(str(code))}</strong> <span aria-hidden="true">·</span> Section: {escape(str(section))}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for _icon, label, value in stats:
            html+= f'<div style="background:#f1f5f3; color:#344640; padding:6px 10px; border-radius:7px; font-size:.9rem">{escape(str(label))}: <b>{escape(str(value))}</b></div>'
        
        html+= "</div>"

    html += "</section>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
