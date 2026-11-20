from ollama import chat

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Explain derivatives in one paragraph."
        }
    ]
)

print(response.message.content)
0

