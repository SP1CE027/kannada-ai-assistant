from app.state import AssistantState
from app.audio import load_audio_info
import time

def main():
    state = AssistantState.IDLE
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.LISTENING
    print(f"STATE → {state.value}")
    time.sleep(1)

    try:
        audio_info = load_audio_info()
        state = AssistantState.PROCESSING
        print(f"STATE → {state.value}")
        print("AUDIO INFO:", audio_info)
    except Exception as e:
        state = AssistantState.ERROR
        print(f"STATE → {state.value}")
        print("ERROR:", e)
        return

    time.sleep(1)

    state = AssistantState.SPEAKING
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.IDLE
    print(f"STATE → {state.value}")

if __name__ == "__main__":
    main()
