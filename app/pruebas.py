from faster_whisper import WhisperModel
import time

model_size = "small"

st=time.time()

# Run on GPU with FP16
#model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")

#Mas adelante hay que deployear con GPU
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio.mp3", beam_size=5,language="es")

#print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

texto=""

for segment in segments: texto+=segment.text
#print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

print(texto)
print(time.time()-st)