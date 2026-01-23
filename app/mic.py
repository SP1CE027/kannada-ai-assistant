import sounddevice as sd
import soundfile as sf
import numpy as np

OUTPUT_PATH = "audio_samples/user_input.wav"

def record_audio(duration=10, sample_rate=16000):
    print(" Recording...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(OUTPUT_PATH, audio, sample_rate)
    print(f" Audio saved to {OUTPUT_PATH}")
