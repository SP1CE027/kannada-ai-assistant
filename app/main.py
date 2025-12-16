from app.state import AssistantState
import time

def main():
    state = AssistantState.IDLE
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.LISTENING
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.PROCESSING
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.SPEAKING
    print(f"STATE → {state.value}")
    time.sleep(1)

    state = AssistantState.IDLE
    print(f"STATE → {state.value}")

if __name__ == "__main__":
    main()
