from services.pdf_loader import extract_text
from services.chunker import chunk_text

text = extract_text("sample.pdf")

chunks = chunk_text(text)

print(f"Chunks: {len(chunks)}")
print()
print(chunks[0])
0

