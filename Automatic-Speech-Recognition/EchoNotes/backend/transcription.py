# backend/transcription.py
import whisper
import tempfile

def transcribe_audio(file_data) -> dict:
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file_data)
        tmp_path = tmp.name
    result = model.transcribe(tmp_path, verbose=False)
    return result
