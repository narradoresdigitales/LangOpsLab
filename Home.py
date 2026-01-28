import streamlit as st
import requests

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="LangOPsTools Dashboard",
    layout="wide"
)

# -----------------------------
# Centered title and description
# -----------------------------
st.markdown("""
<div style="text-align: center;">
    <h1>🛠 LangOPsTools Dashboard</h1>
    <p style="font-size:18px;">Welcome to your AI Language Operations Suite. Use the cards below to access your tools.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Define your tools
# -----------------------------
TOOLS = [
    {
        "name": "Translator",
        "description": "Translate Word documents (.docx) with preview before download. with preview before download.",
        "url": "https://translatetext.streamlit.app/",
        "emoji": "🌍"
    },
    {
        "name": "VidIntel",
        "description": "Experiment with AI agents for planning, executing, and monitoring tasks.",
        "url": "https://vidintel.streamlit.app/",
        "emoji": "🤖"
    },
    {
        "name": "OPI OPS",
        "description": "Placeholder for your next LangOPs tool. Placeholder for your next LangOPs tool.",
        "url": "https://opiops.streamlit.app/",
        "emoji": "🧪"
    }
]

# -----------------------------
# Helper: check if tool is online
# -----------------------------
def check_online(url):
    try:
        response = requests.head(url, timeout=2)
        return response.status_code < 400
    except:
        return False

# -----------------------------
# Responsive columns
# -----------------------------
screen_width = st.sidebar.slider("Simulate screen width (px)", 300, 1920, 1200)
if screen_width >= 1200:
    cols_per_row = 3
elif screen_width >= 768:
    cols_per_row = 2
else:
    cols_per_row = 1

# -----------------------------
# Layout cards with links
# -----------------------------
for i in range(0, len(TOOLS), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, tool in enumerate(TOOLS[i:i+cols_per_row]):
        with cols[j]:
            online = check_online(tool['url']) if tool['url'].startswith("http") else False
            status_color = "#4CAF50" if online else "#f44336"
            status_text = "Online" if online else "Offline"

            st.markdown(f"""
            <div style="
                border:1px solid #ddd; 
                border-radius:10px; 
                padding:20px; 
                margin-bottom:20px; 
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                text-align:center;
                background-color:#f9f9f9;
            ">
                <h3>{tool['emoji']} {tool['name']}</h3>
                <p>{tool['description']}</p>
                <p style="font-weight:bold; color:{status_color};">{status_text}</p>
                <a href="{tool['url']}" target="_blank" style="
                    display:inline-block;
                    padding:10px 20px;
                    background-color:#4CAF50;
                    color:white;
                    text-decoration:none;
                    border-radius:5px;
                    font-weight:bold;
                ">Open Tool</a>
            </div>
            """, unsafe_allow_html=True)
