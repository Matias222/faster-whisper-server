from fastapi import FastAPI, File, UploadFile, Form
from faster_whisper import WhisperModel
from pydub import AudioSegment
import io
import uuid
import time
import os

whisper_amber = FastAPI(
    title="Whisper Amber",
)

@whisper_amber.get("/")
def hola():
    print("Hola")
    return "Hola"

@whisper_amber.post("/upload_audio")
def upload_audio(audio: UploadFile = File(...)):
        
    print("here")

    st=time.time()

    #return
    audio_data = audio.file.read()

    audio = AudioSegment.from_file(io.BytesIO(bytes(audio_data)))
    
    id_audio_local = uuid.uuid4()

    audio.export(f"./{id_audio_local}.mp3", format="mp3")

    model_size = "small"

    #model = WhisperModel(model_size, device="cpu", compute_type="int8")
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    segments, info = model.transcribe(f"./{id_audio_local}.mp3", beam_size=5,language="es")

    texto=""

    for segment in segments: texto+=segment.text

    print(texto,time.time()-st)

    os.remove(f"./{id_audio_local}.mp3")

    return texto