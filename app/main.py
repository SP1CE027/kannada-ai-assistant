from app.state import AssistantState
from pathlib import Path
import time

AUDIO_FILE = Path("audio_samples/user_input.wav")

def main():
    state = AssistantState.IDLE
    print(f"STATE → {state.value}")

    time.sleep(1)

    # Simulate wake word / button
    state = AssistantState.LISTENING
    print(f"STATE → {state.value}")

    time.sleep(1)

    # Simulate audio received
    if AUDIO_FILE.exists():
        state = AssistantState.PROCESSING
        print(f"STATE → {state.value}")
    else:
        state = AssistantState.ERROR
        print(f"STATE → {state.value}")
        return

    time.sleep(1)

    # Simulate response ready
    state = AssistantState.SPEAKING
    print(f"STATE → {state.value}")

    time.sleep(1)

    state = AssistantState.IDLE
    print(f"STATE → {state.value}")

if __name__ == "__main__":
    main()
