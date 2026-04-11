from src.chatbot import Chatbot
from src.utils import append_chat_log


def main() -> None:
    bot = Chatbot(
        system_prompt="You are a senior AI engineer who explains concepts clearly."
    )

    print("Chatbot started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        if not user_input:
            continue

        reply, total_tokens = bot.ask(user_input=user_input, temperature=0.7)

        print(f"AI: {reply}")
        print(f"Tokens used: {total_tokens}\n")

        append_chat_log("logs/chat_log.txt", user_input, reply)


if __name__ == "__main__":
    main()