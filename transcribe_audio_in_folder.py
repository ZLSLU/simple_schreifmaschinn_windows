import numpy as np
import torchaudio
import whisper_timestamped as whisper
from pathlib import Path

AUDIO_DIR   = "audio"
MODEL_PATH  = "pytorch_model.bin"
TARGET_SR   = 16000
DEVICE      = "cpu"

# 1) Load the model once
model = whisper.load_model(MODEL_PATH, device=DEVICE)

def load_audio(path: Path) -> np.ndarray:
    # Load (SoundFile or sox_io backend must be active)
    wav, sr = torchaudio.load(str(path))
    # Stereo → mono
    if wav.shape[0] > 1:
        wav = wav.mean(dim=0, keepdim=True)
    # Resample if needed
    if sr != TARGET_SR:
        wav = torchaudio.transforms.Resample(sr, TARGET_SR)(wav)
    # (1, N) → (N,) float32 in [-1,1]
    return wav.squeeze(0).numpy().astype(np.float32)

def transcribe_folder(folder: str):
    folder = Path(folder)
    for audio_file in sorted(folder.glob("*.*")):
        if audio_file.suffix.lower() not in [".wav", ".flac", ".m4a", ".mp3", ".ogg"]:
            continue

        print(f"Transcribing {audio_file.name}…", end="", flush=True)
        audio_np = load_audio(audio_file)

        # **No** sample_rate kwarg here!
        result = model.transcribe(audio_np)

        # Save
        out_txt = audio_file.with_suffix(".txt")
        out_txt.write_text(result["text"], encoding="utf-8")
        print(" done.")

    print("✅ All done.")

if __name__ == "__main__":
    try:
        transcribe_folder(AUDIO_DIR)
    except Exception as e:
        print("Error:", e)
