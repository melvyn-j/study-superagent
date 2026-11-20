from qdrant_client import QdrantClient
from ollama import embed, chat

client = QdrantClient(
    host="localhost",
    port=6333
)

question = input("Ask a question: ")

query_vector = embed(
    model="nomic-embed-text",
    input=question
)["embeddings"][0]

results = client.query_points(
    collection_name="course_materials",
    query=query_vector,
    limit=3
)

context = "\n\n".join(
    point.payload["text"]
    for point in results.points
)

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "system",
            "content": """
            You are a study tutor.

            Answer ONLY using the supplied lecture notes.

            If the notes don't contain the answer,
            say so clearly.
            """
        },
        {
            "role": "user",
            "content": f"""
Lecture Notes:
{context}

Question:
{question}
"""
        }
    ]
)

print("\nAnswer:\n")
print(response.message.content)
0

