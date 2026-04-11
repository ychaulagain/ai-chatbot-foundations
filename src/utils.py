from pathlib import Path


def append_chat_log(file_path: str, user_input: str, reply: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"AI: {reply}\n")
        f.write("-" * 50 + "\n")