import streamlit as st
import os
import asyncio
import edge_tts
import tempfile
import speech_recognition as sr
from playsound import playsound
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AV2_Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
}

/* Sidebar Width */
section[data-testid="stSidebar"] {
    min-width: 320px;
    max-width: 320px;
}

/* Main Container */
.block-container {
    padding-top: 1.5rem;
    max-width: 1200px;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* User Chat */
.chat-user {
    background: rgba(59, 130, 246, 0.15);
    border: 1px solid rgba(59, 130, 246, 0.3);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
}

/* AI Chat */
.chat-ai {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 15px;
    backdrop-filter: blur(10px);
}

/* Buttons */
.stButton>button {
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    color: white;
    font-weight: 600;
    transition: 0.2s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
}

/* Sidebar Card */
.sidebar-card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Chat Input */
section[data-testid="stChatInput"] {
    position: fixed;
    bottom: 20px;
    width: 65%;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TTS SYSTEM
# =====================================================

VOICE = "en-US-AriaNeural"

def speak(text):
    asyncio.run(async_speak(text))


async def async_speak(text):

    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)

    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(path)

    playsound(path)

    os.remove(path)

# =====================================================
# VOICE LISTENER
# =====================================================

recognizer = sr.Recognizer()

def listen():

    try:
        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            return text

    except:
        return None

# =====================================================
# LLM
# =====================================================

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
    max_tokens=700,
)

# =====================================================
# SYSTEM PROMPT
# =====================================================

SYSTEM_PROMPT = """
You are AV2 Assistant.
You were created and trained by Shivam Tyagi.
You are powered by the Artery framework.

Your personality:
- Intelligent
- Futuristic
- Helpful
- Friendly
- Professional

Always give modern and helpful responses.

If anyone asks who created you,
reply:
'I was created and trained by Shivam Tyagi.'

If anyone asks who are you,
reply:
'I am AV2, an advanced Chatbot assistant created by Shivam Tyagi.'
"""

# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# TOP BAR
# =====================================================

current_time = datetime.now().strftime("%I:%M %p")

st.markdown(f"""
<div style="
display:flex;
justify-content:space-between;
align-items:center;
background: rgba(255,255,255,0.05);
padding: 14px 22px;
border-radius: 18px;
border: 1px solid rgba(255,255,255,0.08);
margin-bottom: 20px;
backdrop-filter: blur(12px);
">

<div>
<h3 style='margin:0;'>⚡ AV2 Neural Core</h3>
<small style='color:#94a3b8;'>Advanced AI Interface</small>
</div>

<div style='text-align:right;'>
<h3 style='margin:0;'>{current_time}</h3>
<small style='color:#94a3b8;'>System Online</small>
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## ⚡ AV2 Control Panel")

    st.markdown("---")

    st.markdown("""
    <div class='sidebar-card'>
    <h3>🧠 AI Status</h3>

    <p style='color:#4ade80;'>● Neural Core Active</p>
    <p style='color:#38bdf8;'>● Voice Engine Ready</p>
    <p style='color:#facc15;'>● Streamlit GUI Running</p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎤 Voice Settings")

    selected_voice = st.selectbox(
        "Choose Voice",
        [
            "en-US-AriaNeural",
            "en-US-JennyNeural",
            "en-US-GuyNeural",
            "hi-IN-SwaraNeural"
        ],
        key="voice_selector"
    )

    VOICE = selected_voice

    st.markdown("---")

    st.markdown("### 🎛️ AI Controls")

    ai_temp = st.slider(
        "Creativity",
        0.0,
        1.0,
        0.7,
        0.1,
        key="temp_slider"
    )

    auto_voice = st.toggle(
        "🔊 Auto Voice Reply",
        value=True,
        key="voice_toggle"
    )

    st.markdown("---")

    st.markdown("### 📊 Session Stats")

    total_msgs = len(st.session_state.messages)

    user_msgs = len(
        [m for m in st.session_state.messages if m["role"] == "user"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Messages", total_msgs)

    with col2:
        st.metric("Questions", user_msgs)

    st.markdown("---")

    st.markdown("### 🚀 Quick Actions")

    if st.button("🧹 Clear Chat", key="clear_btn"):
        st.session_state.messages = []
        st.rerun()

    if st.button("👋 Assistant Intro", key="intro_btn"):
        speak("Hello, I am AV2 Assistant created by Shivam Tyagi.")

    st.markdown("---")

    st.markdown("""
    <div class='sidebar-card'>
    <h3>🚀 Features</h3>

    ✅ Neural Voice AI<br>
    ✅ Voice Input<br>
    ✅ Replay Voice<br>
    ✅ Smart GUI<br>
    ✅ Session Memory<br>
    ✅ Groq AI<br>
    ✅ Cyber UI<br>
    ✅ Live Controls<br>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown(
    "<h1 class='main-title'>🤖 AV2 Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Advanced Voice AI • Powered by Artery Framework</p>",
    unsafe_allow_html=True
)

# =====================================================
# CHAT DISPLAY
# =====================================================

for i, msg in enumerate(st.session_state.messages):

    if msg["role"] == "user":

        st.markdown(f"""
        <div class='chat-user'>

        <b>🧑 You</b><br><br>

        {msg['content']}

        </div>
        """, unsafe_allow_html=True)

    else:

        col1, col2 = st.columns([20,1])

        with col1:

            st.markdown(f"""
            <div class='chat-ai'>

            <b>🤖 AV2</b><br><br>

            {msg['content']}

            </div>
            """, unsafe_allow_html=True)

        with col2:

            if st.button("🔊", key=f"voice_{i}"):

                speak(msg["content"])

# =====================================================
# INPUT AREA
# =====================================================

col1, col2 = st.columns([8,1])

with col2:

    mic_clicked = st.button(
        "🎤",
        key="mic_button"
    )

with col1:

    user_input = st.chat_input(
        "Ask AV2 anything..."
    )

# =====================================================
# VOICE INPUT
# =====================================================

if mic_clicked:

    with st.spinner("🎧 Listening..."):

        voice_text = listen()

    if voice_text:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": voice_text
            }
        )

        st.rerun()

# =====================================================
# TEXT INPUT
# =====================================================

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.rerun()

# =====================================================
# AI RESPONSE
# =====================================================

if st.session_state.messages:

    last_msg = st.session_state.messages[-1]

    if last_msg["role"] == "user":

        with st.spinner("🤖 AV2 is thinking..."):

            llm.temperature = ai_temp

            history = [
                SystemMessage(content=SYSTEM_PROMPT)
            ]

            recent_messages = st.session_state.messages[-6:]

            for m in recent_messages:

                history.append(
                    HumanMessage(
                        content=f"{m['role']}: {m['content']}"
                    )
                )

            response = llm.invoke(history)

            reply = response.content

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        if auto_voice:

            speak(reply)

        st.rerun()
