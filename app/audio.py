from pathlib import Path
import soundfile as sf
import numpy as np
import librosa

RAW_AUDIO = Path("audio_samples/user_input.wav")
NORM_AUDIO = Path("audio_samples/user_input_norm.wav")

def normalize_audio():
    if not RAW_AUDIO.exists():
        raise FileNotFoundError(f"Audio file not found: {RAW_AUDIO}")

    data, sr = sf.read(RAW_AUDIO)

    # stereo → mono
    if data.ndim > 1:
        data = np.mean(data, axis=1)

    # resample to 16kHz
    if sr != 16000:
        data = librosa.resample(data, orig_sr=sr, target_sr=16000)
        sr = 16000

    sf.write(NORM_AUDIO, data, sr)
    return NORM_AUDIO
