🤖 AV2 AI Assistant

AV2 is a futuristic voice-enabled AI assistant built with Python and Streamlit.
It combines a modern cyberpunk-inspired UI with real-time conversational AI, voice interaction, and neural-style system monitoring.

Designed and developed by Shivam Tyagi, AV2 delivers an immersive AI experience with advanced GUI elements, voice synthesis, live metrics, and intelligent conversation capabilities powered by Groq LLM APIs.

🚀 Live Demo

🌐 AV2 AI Assistant Live Demo

✨ Features
🎙️ Real-time Voice Input
🔊 AI Voice Response using Edge TTS
🧠 Groq LLM Integration
⚡ Futuristic Cyberpunk UI
📊 Live System Metrics Dashboard
🎨 Animated Neural Core Interface
💬 Smart Chat Memory
🎤 Multiple Voice Engine Support
🌌 Fully Responsive Streamlit Interface
🖥️ CPU / RAM / GPU Monitoring
🚀 Fast AI Responses
🔐 Secure Environment Variable Support
🛠️ Tech Stack
Technology	Usage
Python	Backend Logic
Streamlit	Frontend UI
Groq API	AI Model Inference
Edge TTS	Text-to-Speech
SpeechRecognition	Voice Input
Psutil	System Metrics
HTML/CSS	Custom Futuristic UI
📂 Project Structure
AV2_Chatbot/
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── assets/
⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/AV2_Chatbot.git
cd AV2_Chatbot

Install dependencies:

pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
▶️ Run Locally
streamlit run streamlit_app.py
📦 Required Modules
streamlit
langchain-groq
langchain-core
edge-tts
playsound==1.2.2
SpeechRecognition
pyaudio
psutil
python-dotenv
🧠 AI Model

AV2 currently uses:

openai/gpt-oss-20b

via Groq ultra-fast inference APIs.

🎤 Voice System

AV2 supports multiple neural voices including:

en-US-AriaNeural
en-US-JennyNeural
en-US-GuyNeural
hi-IN-SwaraNeural

Powered by Microsoft Edge Neural TTS.

🎨 UI Highlights
Glassmorphism Design
Neon Glow Effects
Animated Neural Core
Real-time Status Panels
Cyberpunk Dashboard Layout
Interactive Control Buttons
AI Listening Animation
🔐 Security Note

Never expose your real API keys publicly.

Use:

api_key=os.getenv("GROQ_API_KEY")

instead of hardcoding secrets directly into source code.

📸 Preview

AV2 delivers a cinematic AI interface inspired by futuristic operating systems and neural-core AI environments.

🚀 Future Roadmap
📁 File Upload Support
🧠 Long-Term Memory
🌐 Web Search Integration
🖼️ AI Image Generation
📄 PDF & Document Analysis
🔐 Login & Authentication System
🧩 Plugin Architecture
🖥️ Desktop Version
👨‍💻 Developer

Shivam Tyagi
CSE Student • AI Developer • Futuristic Interface Designer

📜 License

This project is licensed under the MIT License.

⭐ Support

If you like this project, consider giving it a star on GitHub ⭐
