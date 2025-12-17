from pathlib import Path
import wave

AUDIO_PATH = Path("audio_samples/user_input.wav")

def load_audio_info():
    if not AUDIO_PATH.exists():
        raise FileNotFoundError(f"Audio file not found: {AUDIO_PATH}")

    with wave.open(str(AUDIO_PATH), "rb") as wf:
        info = {
            "channels": wf.getnchannels(),
            "sample_width": wf.getsampwidth(),
            "frame_rate": wf.getframerate(),
            "frames": wf.getnframes(),
            "duration_sec": wf.getnframes() / wf.getframerate(),
        }

    return info
