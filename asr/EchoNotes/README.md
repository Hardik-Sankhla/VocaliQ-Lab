# 🎙️ EchoNotes – Voice Memos Reinvented with AI

EchoNotes is a smart, powerful voice memo management app that combines **cutting-edge speech-to-text AI** with an intuitive interface for seamless recording, transcription, and organization of voice notes. Built with Whisper and Streamlit, EchoNotes is your pocket assistant for capturing thoughts, ideas, and meetings on the go.

---

## 🚀 Features

- 🔊 **Voice-to-Text Transcription** – Convert voice memos to accurate text using Whisper by OpenAI.
- ⏱️ **Real-Time Transcription** – See transcriptions while recording, powered by streaming inference.
- 📁 **Memo Dashboard** – View, search, delete, and manage all your past voice notes in one place.
- ☁️ **Cloud Sync Ready** – Designed with future-ready integrations to store memos securely in the cloud.
- 🧪 **FastAPI Backend** – A modular, extendable backend to support API-based operations and deployment.
- 🧠 **LLM-Enhanced Summaries** *(coming soon)* – Get meeting summaries and action items extracted using LLaMA2.

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI (for extensibility)
- **Speech AI**: Whisper (via Ollama)
- **Languages**: Python

---

## ⚙️ Installation & Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hardik-Sankhla/EchoNotes.git
   cd EchoNotes
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the frontend app (Streamlit):**
   ```bash
   streamlit run frontend/app.py
   ```

4. **Run the backend API (FastAPI):**
   ```bash
   uvicorn backend.api:app --reload
   ```

> 🖥️ **Required Terminals:**  
> - Terminal 1: Start Streamlit frontend  
> - Terminal 2: Start FastAPI backend  
> - (Optional) Terminal 3: Start Ollama for Whisper/LLM support

> Note: Ensure `Ollama` is installed and running if you plan to use LLM features.

---

## 📁 File Structure

```bash
EchoNotes/
├── backend/
│   ├── api.py
│   └── utils/
├── frontend/
│   └── app.py
├── assets/
│   └── demo.png
├── requirements.txt
└── README.md
```

---

## 🖼️ Demo

> A quick look at EchoNotes in action:

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/Hardik-Sankhla/Markdown-Resources/main/Image/Demo-EchoNotes.png" alt="EchoNotes Demo">
</div>


---

## 🤝 Contributing

We welcome community contributions to expand EchoNotes! If you have ideas, bug fixes, or new features, feel free to fork and submit a pull request.

---

## 📄 License

MIT License – use it freely, just give credit where it's due.

---

## 👨‍💻 Author

Built with ❤️ by [Hardik Sankhla](https://github.com/Hardik-Sankhla), an open-source enthusiast passionate about creating impactful audio AI tools.

🔗 [View Portfolio](https://github.com/Hardik-Sankhla) • [Follow on Hugging Face](https://huggingface.co/Hardik-Sankha)

> Part of the **[VocaliQ-Lab](https://github.com/Hardik-Sankhla/VocaliQ-Lab)** research initiative on voice, speech, and audio AI.
