# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from . import transcription, ollama_client, schemas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process/", response_model=schemas.AudioProcessResponse)
async def process_audio(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    result = transcription.transcribe_audio(audio_bytes)
    transcript = result["text"]

    summary_prompt = f"Summarize the following meeting transcript:\n\n{transcript}"
    tasks_prompt = f"List all action items from the following meeting:\n\n{transcript}"

    summary = ollama_client.call_ollama(summary_prompt)
    action_items = ollama_client.call_ollama(tasks_prompt)

    return schemas.AudioProcessResponse(
        transcript=transcript,
        summary=summary,
        action_items=action_items
    )