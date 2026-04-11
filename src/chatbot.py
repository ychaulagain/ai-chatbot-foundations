from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from src.config import OPENAI_API_KEY, OPENAI_MODEL


class Chatbot:
    def __init__(self, system_prompt: str = "You are a helpful AI assistant."):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": system_prompt}
        ]

    def ask(self, user_input: str, temperature: float = 0.7) -> tuple[str, int]:
        self.messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=self.messages,
            temperature=temperature,
        )

        reply = response.choices[0].message.content or ""
        total_tokens = response.usage.total_tokens if response.usage else 0

        self.messages.append({"role": "assistant", "content": reply})
        return reply, total_tokens