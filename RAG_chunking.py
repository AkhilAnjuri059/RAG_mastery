## RAG 1st important part load the document
def load_document(path):
    with open(path, "r") as f:
        return f.read()

def chunk_document(text, size=300):
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""
    for para in paragraphs:
        para = para.strip()
        if not para: #if para does not contain anything and empty strings
            continue
        if len(current) + len(para) <= size:
            current = current + "\n\n" + para if current else para #if current contains anything orelse add the para itself
        else:
            chunks.append(current)
            current = para # after dumping the current into chunk the leftover para is added to now new current

    if current:
        chunks.append(current)
    return chunks

text = load_document("sample.txt")
chunks = chunk_document(text)

print(f"Loaded {len(text)} characters → {len(chunks)} chunks\n")
for i, c in enumerate(chunks):
    print(f"--- Chunk {i} ({len(c)} chars) ---")
    print(c)
    print()

