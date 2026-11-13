import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(ellipse at 14% 0%, rgba(30, 91, 87, .08), transparent 34%), #eef1ef !important;
        }
        .stApp div[data-testid="stColumn"] {
            background: #ffffff !important;
            padding: 2rem !important;
            border: 1px solid #d9e0dc !important;
            border-radius: 12px !important;
            box-shadow: 0 10px 30px rgba(24, 39, 34, .06) !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(ellipse at 92% 0%, rgba(30, 91, 87, .055), transparent 32%), #f2f4f2 !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
        :root {
            --ink: #202c29;
            --muted: #66736e;
            --accent: #17685d;
            --accent-hover: #12574f;
            --line: #d9e0dc;
        }
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { max-width: 1180px; padding-top: 2rem !important; padding-bottom: 2.5rem !important; }
        html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; color: var(--ink); }
        h1, h2, h3, h4 {
            color: var(--ink) !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
            letter-spacing: -.035em;
        }
        h1 { font-size: clamp(2.2rem, 4vw, 3.2rem) !important; line-height: 1.08 !important; }
        h2 { font-size: 2rem !important; line-height: 1.15 !important; }
        h3 { font-size: 1.35rem !important; }
        p, label, [data-testid="stMarkdownContainer"] { color: var(--ink); }
        [data-testid="stCaptionContainer"], small { color: var(--muted) !important; }
        .stButton > button {
            min-height: 2.75rem;
            border-radius: 7px !important;
            border: 1px solid var(--line) !important;
            padding: .55rem 1rem !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            transition: background-color .16s ease, border-color .16s ease, transform .16s ease, box-shadow .16s ease !important;
        }
        .stButton > button[kind="primary"] { background: var(--accent) !important; border-color: var(--accent) !important; color: #fff !important; }
        .stButton > button[kind="primary"] p,
        .stButton > button[kind="primary"] [data-testid="stMarkdownContainer"],
        .stButton > button[kind="primary"] span,
        [data-testid="stBaseButton-primary"],
        [data-testid="stBaseButton-primary"] * { color: #fff !important; -webkit-text-fill-color: #fff !important; }
        .stButton > button[kind="primary"]:hover { background: var(--accent-hover) !important; border-color: var(--accent-hover) !important; box-shadow: 0 4px 12px rgba(23, 104, 93, .18); }
        .stButton > button[kind="secondary"] { background: #e7efec !important; border-color: #d4e0db !important; color: #20564e !important; }
        .stButton > button[kind="tertiary"] { background: #fff !important; border-color: var(--line) !important; color: #43514c !important; }
        .stButton > button:hover { transform: translateY(-1px); }
        .stButton > button:focus { box-shadow: 0 0 0 .2rem rgba(23, 104, 93, .2) !important; }
        [data-testid="stTextInput"] input,
        [data-testid="stNumberInput"] input,
        [data-testid="stSelectbox"] [data-baseweb="select"] > div,
        [data-testid="stTextArea"] textarea {
            border-radius: 7px !important;
            border-color: #cbd5d0 !important;
            background: #fff !important;
            color: var(--ink) !important;
            -webkit-text-fill-color: var(--ink) !important;
            caret-color: var(--accent) !important;
        }
        [data-testid="stTextInput"] input::placeholder,
        [data-testid="stNumberInput"] input::placeholder,
        [data-testid="stTextArea"] textarea::placeholder {
            color: #66736e !important;
            -webkit-text-fill-color: #66736e !important;
            opacity: 1 !important;
        }
        [data-testid="stTextInput"] input:-webkit-autofill,
        [data-testid="stNumberInput"] input:-webkit-autofill {
            -webkit-text-fill-color: var(--ink) !important;
            box-shadow: 0 0 0 1000px #fff inset !important;
        }
        [data-testid="stToast"] {
            background: var(--accent) !important;
            color: #fff !important;
            border: 1px solid var(--accent-hover) !important;
            box-shadow: 0 12px 28px rgba(17, 55, 48, .2) !important;
        }
        [data-testid="stToast"] * {
            color: #fff !important;
        }
        [data-testid="stToast"] svg {
            fill: currentColor !important;
        }
        [data-testid="stVerticalBlockBorderWrapper"] { border-color: var(--line) !important; border-radius: 10px !important; }
        [data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 9px; overflow: hidden; }
        hr { border-color: var(--line) !important; }
        @media (max-width: 640px) {
            .block-container { padding: 1rem 1rem 2rem !important; }
            .stApp div[data-testid="stColumn"] { padding: 1.25rem !important; }
        }
        </style>
    """, unsafe_allow_html=True)
