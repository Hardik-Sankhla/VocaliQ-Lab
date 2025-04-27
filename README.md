

<h1 align="center">✨ VocaliQ-Lab</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/Hardik-Sankhla/VocaliQ-Lab/main/docs/diagrams/VocaliQLab%20Banner.png" alt="VocaliQ-Lab Banner">
</p>

### **VocaliQ-Lab**  
**VocaliQ-Lab** is an advanced open-source research lab featuring 30+ cutting-edge **speech, audio, and music AI projects**. Built for researchers, engineers, and enthusiasts, it blends deep learning with sound to push the frontier of audio intelligence.

---

## 🎯 What is VocaliQ-Lab?

A one-stop suite for building, testing, and deploying **AI-driven audio systems**. From speech recognition to music generation and voice biometrics, it offers modular, scalable, and production-ready tools to accelerate innovation in audio AI.

---

## 🔥 Core Features

- 🗣️ **Speech Recognition** – Multilingual, accented, low-resource, whispered, and child/pathological speech support.
- 🎵 **Music AI** – Genre classification, MIDI conversion, music generation, and neural style transfer.
- 🧠 **Audio Intelligence** – Emotion recognition, audio captioning, sound event detection, and fingerprinting.
- 🎧 **Speech Enhancement** – Noise reduction, source separation, super-resolution, and VAD.
- 🔐 **Voice Security** – Speaker identification, verification, deepfake detection.
- 🎥 **Audio-Visual AI** – AV speech recognition, lip-sync, and synchronization.
- 💬 **TTS & Singing** – Text-to-speech synthesis and singing voice generation.
- 🧪 **Interactive Demos** – Gradio and Streamlit-powered web apps and Colab notebooks.
- ⚙️ **Production Ready** – Modular code, Docker support, FastAPI backend, and CI/CD enabled.

---

## 📚 Project Index

| Module         | Project                                  | Colab | Demo | Repo |
|----------------|------------------------------------------|-------|------|------|
| ASR            | [Basic ASR](asr/basic_asr/)              | ✅     | 🔗   | -    |
| Speech         | Multilingual ASR, Whispered Speech       | ✅     | ✅   | -    |
| Enhancement    | [Source Separation](speech_enhancement/source_separation/) | ✅ | 🔗 | - |
| Music AI       | [Genre Classification](music_ai/genre_classification/) | ✅ | 🔗 | - |
| Intelligence   | [Audio Captioning](audio_intelligence/audio_captioning/) | ✅ | 🔗 | - |
| Security       | [Deepfake Detection](security/deepfake_detection/) | ✅ | 🔗 | [GitHub](https://github.com/yourname/deepfake-detection) |
| AV Processing  | AVSR, Lip-Sync, Speaker ID               | ✅     | ✅   | -    |

---

# VocaliQ Lab Architecture

```
VocaliQ-Lab/
│
├── README.md
├── LICENSE
├── .github/
├── docs/
├── common_utils/
├── examples/
│   ├── asr_to_tts/
│   └── separation_to_captioning/
│
├── asr/                             # 🧠 Automatic Speech Recognition
│   ├── basic_asr/                   # Project 681: Speech Recognition System
│   ├── multilingual_asr/            # Project 714: Multilingual Speech Recognition
│   ├── low_resource_asr/            # Project 715: Low-Resource Speech Recognition
│   ├── accented_asr/                # Project 716: Accented Speech Recognition
│   ├── child_asr/                   # Project 717: Child Speech Recognition
│   ├── pathological_asr/            # Project 718: Pathological Speech Recognition
│   ├── whispered_asr/               # Project 719: Whispered Speech Recognition
│   └── speech_to_text_translation/  # Project 713: Speech-to-Text Translation
│
├── tts/                             # 🗣️ Text-to-Speech
│   ├── gtts_basic/                  # Project 689: Text-to-Speech (gTTS)
│   ├── singing_voice/               # Project 698: Singing Voice Synthesis
│   └── voice_conversion/            # Project 690: Voice Conversion System
│
├── speech_enhancement/              # 🎛️ Noise Handling
│   ├── enhancement/                 # Project 685: Speech Enhancement System
│   ├── vad/                         # Project 687: Voice Activity Detection
│   ├── speech_separation/           # Project 686: Speech Separation (Cocktail Party Problem)
│   └── source_separation/           # Project 699: Audio Source Separation
│
├── audio_super_resolution/          # 🔊 Upscaling Audio Quality
│   └── audio_super_resolution/      # Project 700: Audio Super-Resolution
│
├── audio_compression/               # 📦 Audio Compression
│   └── audio_compression/           # Project 701: Audio Compression with Deep Learning
│
├── audio_inpainting/                # 🎨 Audio Restoration
│   └── audio_inpainting/            # Project 702: Audio Inpainting System
│
├── audio_intelligence/              # 🧠 High-Level Audio Understanding
│   ├── emotion_recognition/         # Project 684: Speech Emotion Recognition
│   ├── audio_captioning/            # Project 703: Audio Captioning
│   ├── sound_event_detection/       # Project 704: Sound Event Detection
│   ├── audio_fingerprinting/        # Project 707: Audio Fingerprinting System
│   └── query_by_humming/            # Project 708: Query by Humming Implementation
│
├── security/                        # 🔐 Voice Biometrics + Deepfake
│   ├── speaker_id/                  # Project 682: Speaker Identification
│   ├── speaker_verification/        # Project 683: Speaker Verification
│   └── deepfake_detection/          # Project 720: Audio Deepfake Detection
│
├── av_processing/                   # 🎥 Audio-Visual Systems
│   ├── avsr/                        # Project 705: Audio-Visual Speech Recognition
│   └── av_sync/                     # Project 706: Audio-Visual Synchronization
│
├── music_ai/                        # 🎵 Music Processing
│   ├── genre_classification/        # Project 693: Music Genre Classification
│   ├── musical_instrument_recognition/ # Project 694: Musical Instrument Recognition
│   ├── chord_recognition/           # Project 695: Chord Recognition System
│   ├── beat_tracking/               # Project 696: Beat Tracking Implementation
│   ├── music_generation/            # Project 697: Music Generation System
│   ├── music_style_transfer/        # Project 711: Music Style Transfer
│   ├── audio_to_midi/               # Project 712: Audio-to-MIDI Conversion
│   └── cover_song_identification/   # Project 709: Cover Song Identification
│
├── recommendation/                  # 🎧 Music Suggestion
│   └── music_recommender/           # Project 710: Music Recommendation System
│
├── speech_segmentation/             # ✂️ Speech Units
│   └── speech_segmentation/         # Project 688: Automatic Speech Segmentation
│
├── submodules/                      # 💡 External Tools
│   └── spleeter/                    # Using for advanced source separation
│
└── tests/                            # ✅ Unit & integration tests
    └── test_audio_pipeline.py

```

---
## 👤 Author

<div align="center">

[![GitHub WidgetBox](https://github-widgetbox.vercel.app/api/profile?username=Hardik-Sankhla&data=followers,repositories,stars,commits&theme=dracula)](https://github.com/Hardik-Sankhla/)

**Hardik Sankhla**  
🎓 Data Science Student - AI & ML Engineer | 🌟 Open Source Contributor | Oracle Certified OCI Generative AI Professional | OCI Foundation Associate | OCI DATA Associate | OCI AI Associate 



<div align="center">
  <a href="https://www.youtube.com/">
    <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="YouTube logo" />
  </a>
  <a href="https://twitter.com/hardik_sankhla">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="Twitter logo" />
  </a>
</div>

<p align="center">
  <a href="https://linkedin.com/in/hardik-sankhla"><img src="https://img.shields.io/badge/LinkedIn-Hardik%20Sankhla-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>
  <a href="https://github.com/Hardik-Sankhla"><img src="https://img.shields.io/badge/GitHub-Hardik%20Sankhla-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="mailto:datascientist.hardiksankhla@email.com"><img src="https://img.shields.io/badge/Email-datascientist.hardiksankhla%40email.com-red?style=for-the-badge&logo=gmail" alt="Email"></a>
  <a href="https://dataxhardik.wixsite.com/myportfolio"><img src="https://img.shields.io/badge/Portfolio-Hardik%20Sankhla-ff69b4?style=for-the-badge&logo=appveyor" alt="Portfolio"></a>
</p>

📝 [PeerList](https://peerlist.io/hardiksankhla) | ✉️ [Email Me](mailto:datascientist.hardikSankhla@gmail.com)

</div>

<br>

<p align="left">I'm Hardik Sankhla from Jodhpur, I am a passionate software developer with a keen interest in building scalable and efficient applications. I enjoy working with modern web technologies and continuously learning new things to enhance my skills. <br><br>

- 🔭 I’m working as AI Intern at Gyan Netra<br>
- 📚 I'm currently learning Generative AI <br>
- ⚡ In my free time, I explore AI Agents & Agentic AI<br>
- 🎓 Data Science student at JIET Institute of Design and Technology<br>
- 💼 Skilled in Data Analytics, Visualization, ML, and Cloud Computing<br>
- 💡 Eager to contribute innovative solutions in both Data Science and Cloud domains<br>
- 🌱 Currently learning advanced concepts in Deep Learning
</p>

---

## 📘 Documentation

👉 Visit the official docs and tutorials: [yourusername.github.io/vocaliq-lab](https://yourusername.github.io/vocaliq-lab)

---

## 🧰 Tech Stack

- **ML/DL Frameworks**: PyTorch, TensorFlow, Hugging Face
- **Audio Processing**: Librosa, Torchaudio, Pydub
- **Visualization**: Matplotlib, Plotly
- **Deployment**: FastAPI, Docker
- **Demos**: Gradio, Streamlit
- **Automation**: GitHub Actions, Google Colab

---

## 🤝 Join the Mission

We’re building the future of Audio AI. Contributions, collaborations, and feedback are welcome!  
Check out [CONTRIBUTING.md](CONTRIBUTING.md) to get started.


---
F i x   f o r   s t r e a k  
 