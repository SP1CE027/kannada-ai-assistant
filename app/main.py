from app.state import AssistantState
from app.mic import record_audio
from app.audio import normalize_audio
import time

def main():
    state = AssistantState.IDLE
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.LISTENING
    print(f"STATE → {state.value}")

    record_audio(duration=10)

    try:
        norm_path = normalize_audio()
        state = AssistantState.PROCESSING
        print(f"STATE → {state.value}")
        print("NORMALIZED AUDIO:", norm_path)
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
