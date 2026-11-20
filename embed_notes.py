from ollama import embed

response = embed(
    model="nomic-embed-text",
    input="The derivative measures the rate of change of a function."
)

print(len(response["embeddings"][0]))
0

