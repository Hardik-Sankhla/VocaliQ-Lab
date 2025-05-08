# frontend/app.py
import streamlit as st
import requests

st.set_page_config(page_title="EchoNotes - AI Meeting Summarizer")
st.title("🎙 EchoNotes - AI Meeting Notes Generator")

audio_file = st.file_uploader("Upload a meeting audio file (mp3/wav)", type=["mp3", "wav"])

if audio_file:
    st.audio(audio_file)
    if st.button("Generate Notes"):
        with st.spinner("Processing audio and generating notes..."):
            res = requests.post(
                "http://localhost:8000/process/",
                files={"file": (audio_file.name, audio_file, audio_file.type)}
            )
            if res.status_code == 200:
                output = res.json()
                st.subheader("📝 Summary")
                st.write(output["summary"])

                st.subheader("✅ Action Items")
                st.write(output["action_items"])

                st.subheader("📄 Transcript")
                st.text_area("Transcript", output["transcript"], height=300)

                st.download_button("Download Transcript", output["transcript"], file_name="transcript.txt")
            else:
                st.error("Failed to process audio. Please try again.")