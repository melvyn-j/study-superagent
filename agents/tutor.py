from ollama import chat

def tutor_agent(question: str):

    response = chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert tutor. "
                    "Explain concepts clearly, use examples, "
                    "and keep answers concise."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.message.content


if __name__ == "__main__":
    answer = tutor_agent(
        "What is the chain rule in calculus?"
    )

    print(answer)
0

