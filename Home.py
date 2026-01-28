import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="LangOPsTools Dashboard",
    layout="wide"
)

st.title("🛠 LangOPsTools")
st.markdown(
    """
Welcome to your **AI Language Operations Dashboard**.  
Use the cards below to access your tools for translation, agent experiments, and more.
"""
)

# -----------------------------
# Define your tools
# -----------------------------
TOOLS = [
    {
        "name": "Document Translator",
        "description": "Translate Word documents (.docx) to multiple languages with preview before download.",
        "url": "https://your-translator-app.streamlit.app",
        "emoji": "🌍"
    },
    {
        "name": "Agent Lab",
        "description": "Experiment with AI agents for tasks like planning, executing, and monitoring.",
        "url": "https://your-agent-app.streamlit.app",
        "emoji": "🤖"
    },
    {
        "name": "Future Tool",
        "description": "Placeholder for your next LangOPs tool.",
        "url": "#",
        "emoji": "🧪"
    }
]

# -----------------------------
# Layout the cards
# -----------------------------
cols = st.columns(len(TOOLS))

for i, tool in enumerate(TOOLS):
    with cols[i]:
        st.markdown(f"### {tool['emoji']} {tool['name']}")
        st.write(tool["description"])
        st.markdown(f"[Open Tool]({tool['url']})")
